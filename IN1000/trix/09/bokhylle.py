from bok import Book

class Bookshelf:

    def __init__(self):

        self._books = []

    def available(self):

        if len(self._books) < 11:
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
        print("Did not find it")
        return False

bokhylle = Bookshelf()
bok1 = Book("test", "Ola", 2023)
bokhylle.add_book(bok1)
bokhylle.find_book("test", 2023)
bokhylle.find_book("hei", 2102)
print(bokhylle.available())
