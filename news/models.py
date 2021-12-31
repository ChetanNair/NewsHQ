from django.db import models
from datetime import date


class Website(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.TextField()
    parent_website = models.ForeignKey(Website, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
