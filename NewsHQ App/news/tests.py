from django.test import TestCase
from .models import Article, Website


class ArticleTestCase(TestCase):
    def setUp(self):
        self.website_ = "https:retuers.com"
        self.website = Website.objects.create(url=self.website_)
        self.article = Article.objects.create(
            title="Testing",
            text="Testing Text",
            url="https://reuters.com/testing",
            parent_website=self.website,
        )

    def test_website_article_fk(self):
        self.assertEqual(self.article.parent_website, self.website_)


class WebsiteTestCase(TestCase):
    def setUp(self):
        self.website = Website.objects.create(url="https://reuters.com")
        self.website = Website.objects.create(url="https://apnews.com")
