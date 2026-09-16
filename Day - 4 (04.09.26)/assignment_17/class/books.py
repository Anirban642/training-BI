from exceptions import DuplicateBookError, BookNotFoundError, IssuedBookError

class Book:
    def __init__(self, id, title, author, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

class BookManager:
    def __init__(self):
        self.books = [
            Book(1, "Inglorious Empire", "Sashi Tharoor"),
            Book(2, "Wings of Fire", "A. P. J. Abdul Kalam"),
            Book(3, "The Alchemist", "Paulo Coelho"),                Book(4, "Atomic Habits", "James Clear"),
            Book(5, "Harry Potter", "J. K. Rowlig"),
            Book(6, "The Hobbit", "J. R. R. Tolkien"),                Book(7, "Rich Dad Poor Dad", "Robert Kiyosaki"),
            Book(8, "Ikigai", "Hector Garcia")
        ]

    def add_book(self, id, title, author):
        for book in self.books:
            if book.id == id:
                raise DuplicateBookError("Book ID already exists")
        book = Book(id, title, author)
        self.books.append(book)

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                if not book.available:
                    raise IssuedBookError("Cannot remove an issued book")
                self.books.remove(book)
                return
        raise BookNotFoundError("Book not found")

    def search_book(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def get_book(self, id):
        for book in self.books:
            if book.id == id:
                return book
        raise BookNotFoundError("Book not found")

    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book)
        return available_books

    def list_issued_books(self):
        issued_books = []
        for book in self.books:
            if not book.available:
                issued_books.append(book)
        return issued_books