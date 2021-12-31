from django.shortcuts import render
from .models import Article, Website
import newspaper
from .forms import URLForm
from datetime import date


def scrape(parent_website_result):

    Article.objects.filter(parent_website=parent_website_result).delete()

    count = 0
    try:
        paper = newspaper.build(
            parent_website_result.url, memoize_articles=False)
        for article in paper.articles[0:3]:

            article.download()
            article.parse()
            if len(article.text) < 400:

                Article.objects.create(
                    title=article.title, url=article.url, parent_website=parent_website_result, count=count, text=article.text + "...")
            else:

                Article.objects.create(
                    title=article.title, url=article.url, parent_website=parent_website_result, count=count, text=article.text[0:400] + "...")
            count += 1
    except:
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=0, text="Please try another website")
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=1, text="Please try another website")
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=2, text="Please try another website")

    return parent_website_result


def update(parent_website_url):
    parent_website_result = Website.objects.filter(
        url=parent_website_url).first()
    if parent_website_result:

        if len(list(parent_website_result.article_set.all())) == 3:

            return parent_website_result

        parent_website_result = scrape(parent_website_result)
        return parent_website_result
    else:
        parent_website_result = Website.objects.create(url=parent_website_url)

        parent_website_result = scrape(parent_website_result)
        return parent_website_result


def clean():
    Article.objects.exclude(date=date.today()).delete()
    Article.objects.filter(title__endswith=" is not responding").delete()


def display(request):
    clean()
    parent_website_urls = ["https://bbc.co.uk",
                           "https://apnews.com", "https://reuters.com"]

    form = URLForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            parent_website_urls = [form['url1'].value(), form['url2'].value(),
                                   form['url3'].value()]

    articles = []

    for parent_website_url in parent_website_urls:

        parent_website_result = update(parent_website_url)

        for article in parent_website_result.article_set.all():
            articles.append(article)

    articles = list(set(articles))

    context = {'articles': articles,
               'parent_website_urls': parent_website_urls, 'form': form}

    return render(request, "news/home.html", context)
