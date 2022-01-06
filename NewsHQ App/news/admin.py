from django.contrib import admin
from .models import Article, Website

# Models are registered here so that they can seen on the admin page.
admin.site.register(Article)
admin.site.register(Website)
