from django.db import models

# Create your models here.
class NewsSource(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    feed = models.URLField(max_length=256)
    retrieved_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=2, default="US")
    timezone = models.CharField(max_length=2, default="US")

class NewsArticle(models.Model):
    source = models.ForeignKey('NewsSource', on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=256, unique=False)
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=False)
    added_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    description = models.TextField()
    