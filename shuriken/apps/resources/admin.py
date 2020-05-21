from django.contrib import admin
from .models import NewsSource, NewsArticle
# Register your models here.

admin.site.register(NewsSource)
admin.site.register(NewsArticle)