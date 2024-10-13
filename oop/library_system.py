# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class for PrintBooks
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library class to manage books
class Library:
    def __init__(self):
        """Initialize an empty list to store books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print all the books currently in the library."""
        for book in self.books:
            print(book)
