class Book:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
    
    def __str__(self):
        return f"{self._author}: {self._title}, {self._year}"

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_author(self):
        return self._author


