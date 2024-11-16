from bok import Book
from bokhylle import Bookshelf
from bibliotek import Library

def main():
    book1 = Book("Jeg var der", "Mats Andersen", "2025")
    book2 = Book("Jeg var IKKE der", "Mats Andersen", "2026")
    book3 = Book("Overalt og ingensteds", "Mats Andersen", "2027")
    book4 = Book("Verdensaltet", "Mats Andersen", "2027")
    book5 = Book("Liv gjennom ledninger", "Mats Andersen", "2027")
    book6 = Book("Blaatt lys", "Mats Andersen", "2031")
    
    books = [book1,book2,book3,book4,book5,book6]

    library = Library()

    for book in books:
        library.addbook(book)

    library.find("Jeg var der", "2025")
    library.find("Hoho", "2303")
    print(library)

if __name__ == "__main__":
    main()
