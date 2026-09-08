from books import BookManager
from users import UserManager
from exceptions import UserNotFoundError, BookUnavailableError, BookNotIssuedError

class Library:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()

    def issue_book(self, book_id, user_id):
        self.user_manager.get_user(user_id)
        book = self.book_manager.get_book(book_id)
        if not book.available:
            raise BookUnavailableError("Book is not available")
        book.available = False

    def return_book(self, book_id):
        book = self.book_manager.get_book(book_id)
        if book.available:
            raise BookNotIssuedError("Book is not issued")
        book.available = True