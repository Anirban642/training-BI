from exceptions import DuplicateBookError, BookNotFoundError, IssuedBookError

def add_book(books, id, title, author):
    for book in books:
        if book["id"] == id:
            raise DuplicateBookError("Book ID already exists")
    book = {
        "id": id,
        "title": title,
        "author": author,
        "available": True
    }
    books.append(book)

def remove_book(books, id):
    for book in books:
        if book["id"] == id:
            if not book["available"]:
                raise IssuedBookError("Cannot remove an issued book")
            books.remove(book)
            return
    raise BookNotFoundError("Book not found")

def search_book(books, keyword):
    found_books = []
    for book in books:
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            found_books.append(book)
    return found_books

def get_book(books, id):
    for book in books:
        if book["id"] == id:
            return book
    raise BookNotFoundError("Book not found")

def list_available_books(books):
    available_books = []
    for book in books:
        if book["available"]:
            available_books.append(book)
    return available_books

def list_issued_books(books):
    issued_books = []
    for book in books:
        if not book["available"]:
            issued_books.append(book)
    return issued_books