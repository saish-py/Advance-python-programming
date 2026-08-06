class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron_id, book_id):
        for p in self.patrons:
            if p.patron_id == patron_id:
                for b in self.books:
                    if b.book_id == book_id and b.available:
                        b.available = False
                        p.borrowed.append(b.title)
                        print(p.name, "borrowed", b.title)
                        return
        print("Book not available")

    def return_book(self, patron_id, book_id):
        for p in self.patrons:
            if p.patron_id == patron_id:
                for b in self.books:
                    if b.book_id == book_id and b.title in p.borrowed:
                        b.available = True
                        p.borrowed.remove(b.title)
                        print(p.name, "returned", b.title)
                        return
        print("Book not found")

    def show_books(self):
        for b in self.books:
            if b.available:
                print(b.book_id, b.title, "- Available")
            else:
                print(b.book_id, b.title, "- Borrowed")


library = Library()

library.add_book(Book(1, "Python"))
library.add_book(Book(2, "Java"))

library.add_patron(Patron(101, "Shreya"))
library.add_patron(Patron(102, "Rahul"))

library.show_books()

library.borrow_book(101, 1)

library.show_books()

library.return_book(101, 1)

library.show_books()
