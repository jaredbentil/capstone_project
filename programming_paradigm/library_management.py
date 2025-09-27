# Your Task: library_management.py
# Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        return [book.title for book in self._books if book.is_available()]
    
# Example usage:
if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    print("Available books:", library.list_available_books())

    if library.check_out_book("1984"):
        print("Checked out '1984'")
    else:
        print("'1984' is not available")

    print("Available books after checkout:", library.list_available_books())

    if library.return_book("1984"):
        print("Returned '1984'")
    else:
        print("'1984' was not checked out")

    print("Available books after return:", library.list_available_books())          


# This code defines a simple library management system with classes for Book and Library, demonstrating encapsulation and basic OOP principles.