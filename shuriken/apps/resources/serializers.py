from rest_framework import serializers
from .models import NewsSource, NewsArticle

class NewsSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsSource
        fields = ('id', 'name', 'url')
        
class NewsArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsArticle
        fields = ('id', 'source', 'url', 'title', 'created_at', 'added_at', 'body')
