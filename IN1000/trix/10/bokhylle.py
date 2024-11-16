from bok import Book

class Bookshelf:

    def __init__(self):

        self._books = []
    
    def __str__(self):
        return "\n".join([str(book) for book in self._books])
    def available(self):

        if len(self._books) < 2:
            return True
        else:
            return False

    def add_book(self, book):

        if self.available():
            self._books.append(book)
            return True
        else:
            return False
    
    def find_book(self, title, year):
        
        for item in self._books:
            if item.get_title() == title and item.get_year() == year:
                print(f"Found {item}")
                return True
        return False

