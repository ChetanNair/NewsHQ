from django.db import models
from datetime import date

# News website URLs are held here. This acts as a Foreign key to the parent_website field in the Article table.


class Website(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url

# Holds 3 articles from each of the news websites in the Website table.


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.TextField()
    parent_website = models.ForeignKey(Website, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
