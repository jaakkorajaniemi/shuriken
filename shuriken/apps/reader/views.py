from django.shortcuts import render
from shuriken.apps.blog.models import Post
from .models import Book, Chapter

# Create your views here.
def index(request):

   book = Book.objects.get(pk=1)
   chapters = Chapter.objects.filter(book=1)

   context = {
      'book': book,
      'chapters': chapters
   }

   return render(request, 'reader/index.html', context)
