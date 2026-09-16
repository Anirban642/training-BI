from books import add_book, remove_book, search_book, get_book, list_available_books, list_issued_books
from users import register_user
from library import issue_book, return_book
from validators import validate_id, validate_name, validate_text
from exceptions import *

books = [
    {"id": 1, "title": "Inglorious Empire", "author": "Sashi Tharoor", "available": True},
    {"id": 2, "title": "Wings of Fire", "author": "A. P. J. Abdul Kalam", "available": True},
    {"id": 3, "title": "The Alchemist", "author": "Paulo Coelho", "available": True},
    {"id": 4, "title": "Atomic Habits", "author": "James Clear", "available": True},
    {"id": 5, "title": "Harry Potter", "author": "J. K. Rowling", "available": True},
    {"id": 6, "title": "The Hobbit", "author": "J. R. R. Tolkien", "available": True},
    {"id": 7, "title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "available": True},
    {"id": 8, "title": "Ikigai", "author": "Hector Garcia", "available": True}
]

users = [
    {"id": 1, "name": "Pritam"},
    {"id": 2, "name": "Anirban"},
    {"id": 3, "name": "Ashmita"},
    {"id": 4, "name": "Tarun"},
    {"id": 5, "name": "Alinda"}
]

while True:
    print("\n1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Register user")
    print("5. Issue book")
    print("6. Return book")
    print("7. List available books")
    print("8. List issued books")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author: ")
            validate_id(id)
            validate_text(title)
            validate_text(author)
            add_book(books, id, title, author)
            print("Book added successfully")
        except ValueError as e:
            print(e)
        except DuplicateBookError as e:
            print(e)

    elif choice == "2":
        try:
            id = int(input("Enter book ID: "))
            validate_id(id)
            remove_book(books, id)
            print("Book removed successfully")
        except ValueError as e:
            print(e)
        except BookNotFoundError as e:
            print(e)
        except IssuedBookError as e:
            print(e)

    elif choice == "3":
        try:
            keyword = input("Enter title or author to search: ")
            validate_text(keyword)
            found_books = search_book(books, keyword)
            if found_books:
                for book in found_books:
                    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
            else:
                print("No books found")
        except ValueError as e:
            print(e)

    elif choice == "4":
        try:
            id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            validate_id(id)
            validate_name(name)
            register_user(users, id, name)
            print("User registered successfully")
        except ValueError as e:
            print(e)
        except DuplicateUserError as e:
            print(e)

    elif choice == "5":
        try:
            book_id = int(input("Enter book ID: "))
            user_id = int(input("Enter user ID: "))
            validate_id(book_id)
            validate_id(user_id)
            issue_book(books, users, book_id, user_id)
            print("Book issued successfully")
        except ValueError as e:
            print(e)
        except BookNotFoundError as e:
            print(e)
        except UserNotFoundError as e:
            print(e)
        except BookUnavailableError as e:
            print(e)

    elif choice == "6":
        try:
            book_id = int(input("Enter book ID: "))
            validate_id(book_id)
            return_book(books, book_id)
            print("Book returned successfully")
        except ValueError as e:
            print(e)
        except BookNotFoundError as e:
            print(e)
        except BookNotIssuedError as e:
            print(e)

    elif choice == "7":
        available_books = list_available_books(books)
        if available_books:
            for book in available_books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
        else:
            print("No available books")

    elif choice == "8":
        issued_books = list_issued_books(books)
        if issued_books:
            for book in issued_books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
        else:
            print("No issued books")

    elif choice == "9":
        print("Thank you for using the library system")
        break

    else:
        print("Invalid choice")