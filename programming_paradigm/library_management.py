# library_management.py

class Book:
    """Represents a single book with title, author, and check-out status."""

    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and provides operations on them."""

    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds and checks out a book by its title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break  # Only one book should be checked out at a time

    def return_book(self, title):
        """Finds and returns a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                break

    def list_available_books(self):
        """Prints all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
