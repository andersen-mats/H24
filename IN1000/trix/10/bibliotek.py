from bokhylle import Bookshelf

class Library:

    def __init__(self):

        self._bookshelfs = list()

    def __str__(self):
        return "\n".join(str(shelf) for shelf in self._bookshelfs)
    def add_bookshelf(self, shelf):

        self._bookshelfs.append(shelf)

    def find(self, title, year):

        for shelf in self._bookshelfs:
            if shelf.find_book(title, year):
                return True
        print("Did not find it anywhere")
        return False

    def addbook(self,book):
        for shelf in self._bookshelfs:
            if shelf.add_book(book):
                return True
        self.add_bookshelf(Bookshelf())
        self.addbook(book)
