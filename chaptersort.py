import os

class Book:
    tree = []

    def build(self, chapters):
        for x in chapters:
            self.insert(x)
        
    def insert(self, chapter):
        ptr = self.tree

        # check if chapter exists
        f = chapter.exists(self)
        if f is not False:
            return f

        else: # otherwise look for a place to insert
            if chapter.parent is not None: # we might have to add the parent first
                ptr = self.insert(chapter.parent)
            
            ptr.append([chapter, []])
            ptr = ptr[(len(ptr)-1)][1] # revise pointer to the newly appended chapter
            return ptr

class Chapter:
    parent = None
    id = 0
    desc = '?.?'

    def __init__(self, id, desc, parent):
        self.id = id
        self.desc = desc
        self.parent = parent

    def __str__(self):
        return 'Chapter(' + self.desc + ')'

    
    def __repr__(self):
        return 'Chapter(' + self.desc + ')'

    # Returns parent node in chapter tree if found, False if not found.
    def exists(self, book, ptr=None):
        found = False
        
        if ptr == None:
            ptr = book.tree

        for x in ptr:
            # if found
            if x[0].id == self.id:
                return ptr
            # if not found, continue search
            else:
                found = self.exists(book, x[1])

        return found

c4 = Chapter(id=2, desc='2.0', parent=None)
c5 = Chapter(id=3, desc='3.0', parent=None)
c2 = Chapter(id=1, desc='1.0', parent=None)
c1 = Chapter(id=4, desc='1.1', parent=c2)
c3 = Chapter(id=5, desc='1.2', parent=c1)

chapters = []
chapters.append(c1)
chapters.append(c2)
chapters.append(c3)
chapters.append(c4)
chapters.append(c5)

print("Found raw chapter list:")
print(chapters)

book = Book()
book.build(chapters)

print("Printing final tree:")

print(book.tree)
