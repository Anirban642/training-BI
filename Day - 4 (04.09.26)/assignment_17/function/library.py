from books import get_book
from users import get_user
from exceptions import BookUnavailableError, BookNotIssuedError

def issue_book(books, users, book_id, user_id):
    get_user(users, user_id)
    book = get_book(books, book_id)
    if not book["available"]:
        raise BookUnavailableError("Book is not available")
    book["available"] = False

def return_book(books, book_id):
    book = get_book(books, book_id)
    if book["available"]:
        raise BookNotIssuedError("Book is not issued")
    book["available"] = True