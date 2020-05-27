from django.db import models
from shuriken.apps.blog.models import Post

# Create your models here.
class Book(models.Model):
    tree = []

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

    # build chapter tree
    def build(self, chapters):

        if len(self.tree) > 0:
            return False

        for x in chapters:
            self.insert(x)
        
        print(self.tree)
        return True

    # insert chapter to chapter tree  
    def insert(self, chapter):
        print("Inserting chapter (id:" + str(chapter) + ") (p: " + str(chapter.parent) + ")")
        ptr = self.tree

        # check if chapter exists
        f = chapter.exists(self)
        if f is not False:
            print("  ... exists, aborting")
            return f

        else: # otherwise look for a place to insert
            print("  ... not found, finding place to insert")
            if chapter.parent is not None: # we might have to add the parent first
                print("  ... need to add parent first")
                ptr = self.insert(chapter.parent)
            
            print("  ... finally inserting chapter (id:" + str(chapter) + ") (p: " + str(chapter.parent) + ")")
            ptr.append([chapter, []])
            ptr = ptr[(len(ptr)-1)][1] # revise pointer to the newly appended chapter
            return ptr

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

    def __str__(self):
        return str(self.id)
    
    def exists(self, book, ptr=None):
        found = False
        
        if ptr == None:
            ptr = book.tree

        for x in ptr:
            # if found
            if x[0].id == self.id:
                return x[1]
            # if not found, continue search
            else:
                found = self.exists(book, x[1])

        return found