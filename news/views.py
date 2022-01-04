from django.shortcuts import render
from .models import Article, Website
import newspaper
from .forms import URLForm
from datetime import date

# Scrapes the website passed in and creates entries in the database. The website is added to the Website table and the articles
# are added to the Article table. Each article has a parent website foreign key field that links to the Website table records.


def scrape(parent_website_result):

    # Clears any residue articles in case less than 3 articles were obtained on a previous scrape.
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
        # Unresponsive website will lead to this message being added into the slides so that users know the website they have entered is not responding to requests from NewsHQ
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=0, text="Please try another website")
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=1, text="Please try another website")
        Article.objects.create(
            title=parent_website_result.url + " is not responding", url=parent_website_result.url, parent_website=parent_website_result, count=2, text="Please try another website")

    return parent_website_result

# Updates the database with the entered website and articles if they don't already exist within the database.
# The database "remembers" previously loaded websites always and articles if they were scraped "today".


def update(parent_website_url):
    parent_website_result = Website.objects.filter(
        url=parent_website_url).first()

    # This checks whether the website is already in the database
    if parent_website_result:

        # This then checks whether 3 articles already exists within the database, in which case no updating is done.
        if len(list(parent_website_result.article_set.all())) == 3:

            return parent_website_result

        # If the number of articles isn't 3, then the website is scraped and articles are added to the database.
        parent_website_result = scrape(parent_website_result)
        return parent_website_result
    else:

        # If the website doesn't exist in the database, it's added and is scraped to get articles.
        parent_website_result = Website.objects.create(url=parent_website_url)

        parent_website_result = scrape(parent_website_result)
        return parent_website_result

# Cleans up unresponsive page messages and also outdated articles—articles not published "today"


def clean():
    Article.objects.exclude(date=date.today()).delete()
    Article.objects.filter(title__endswith=" is not responding").delete()

# This is the function that displays the content and services input URL from the frontend.


def display(request):
    clean()

    # Starting websites as a default
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
