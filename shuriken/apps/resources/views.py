from django.shortcuts import render
from .models import NewsSource, NewsArticle
from .serializers import NewsArticleSerializer, NewsSourceSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    sources = NewsSource.objects.all()
    articles = NewsArticle.objects.all()

    context = {
        'sources': sources,
        'articles': articles
    }

    return render(request, 'resources/index.html', context)

class NewsSourcesListCreate(generics.ListCreateAPIView):
    queryset = NewsSource.objects.all()
    serializer_class = NewsSourceSerializer
    
class NewsArticlesListCreate(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all().order_by('-created_at')
    serializer_class = NewsArticleSerializer