from django.db import models
from shuriken.apps.blog.models import Post

# Create your models here.
class Book(models.Model):
    # Extended Post object from the blog app
    data = models.ForeignKey(Post, on_delete=models.PROTECT)

    # post.title is used as the book title
    # post.content is used as the book backcover description
    # post.language is used as the book language
    # post.visible is evaluated for public visibility of the book
    
    isbn = models.CharField(max_length=16, default=None, null=True)

    # Generate PDF
    def convert(self):
        pass

class Chapter(models.Model):
    parent = models.ForeignKey('Chapter', on_delete=models.CASCADE, blank=True, null=True, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Extended Post object from the blog app
    data = models.ForeignKey(Post, on_delete=models.PROTECT)

    # post.title is used as the chapter title
    # post.content is used as the chapter content
    # post.language is used as the chapter language
    # post.visible is evaluated for public visibility of the chapter

    # Chapter order if there are multiple chapters with the same parent
    order = models.IntegerField(default=0, null=False)

    # Generate PDF
    def convert(self):
        pass
