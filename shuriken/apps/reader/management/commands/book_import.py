from django.core.management.base import BaseCommand
from shuriken.apps.blog.models import Post
from shuriken.apps.reader.models import Book, Chapter
import random
import lorem

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'This command programmatically imports a book file into Shuriken'

    def _create_book(self):
        posts = []
        chapters = []
        book = None

        for _ in range(80):
            post = Post(pk=_+1)
            post.created_at = '2005-05-05 05:15:25+00:00'
            post.updated_at = '2005-05-05 05:15:25+00:00'
            post.title = lorem.sentence()
            post.description = lorem.paragraph()
            post.content = lorem.paragraph()
            post.static = True
            post.extended = True
            post.save()
            posts.append(post)
            print("Generated Post (id: " + str(post.pk) + ")")
        
        book = Book()
        book.pk = 1
        book.isbn = "abc123456789"
        book.data = posts[0]
        book.save()
        print("Generated Book (id: " + str(book.pk) + ")")

        for _ in range(4):
            chapter = Chapter(pk=_+1)
            chapter.book = book
            chapter.parent = None
            chapter.data = posts[_+1]
            chapter.order = 0
            chapter.save()
            chapters.append(chapter)
            print("Generated Chapter (id: " + str(chapter.pk) + ")")

        for _ in range(75):
            chapter = Chapter(pk=_+5)
            chapter.book = book
            chapter.parent = chapters[random.randint(0,3+_-1)]
            chapter.data = posts[_+5]
            chapter.order = 0
            chapter.save()
            chapters.append(chapter)
            print("Generated Chapter (id: " + str(chapter.pk) + ")")

        print("Import finished.")

    def handle(self, *args, **options):
        self._create_book()