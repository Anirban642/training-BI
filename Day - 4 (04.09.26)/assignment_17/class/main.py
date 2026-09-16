from library import Library
from validators import validate_id, validate_name, validate_text
from exceptions import *

library = Library()

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
            library.book_manager.add_book(id, title, author)
            print("Book added successfully")
        except ValueError as e:
            print(e)
        except DuplicateBookError as e:
            print(e)

    elif choice == "2":
        try:
            id = int(input("Enter book ID: "))
            validate_id(id)
            library.book_manager.remove_book(id)
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
            books = library.book_manager.search_book(keyword)
            if books:
                for book in books:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
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
            library.user_manager.register_user(id, name)
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
            library.issue_book(book_id, user_id)
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
            library.return_book(book_id)
            print("Book returned successfully")
        except ValueError as e:
            print(e)
        except BookNotFoundError as e:
            print(e)
        except BookNotIssuedError as e:
            print(e)

    elif choice == "7":
        books = library.book_manager.list_available_books()
        if books:
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No available books")

    elif choice == "8":
        books = library.book_manager.list_issued_books()
        if books:
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No issued books")

    elif choice == "9":
        print("Thank you for using the library system")
        break

    else:
        print("Invalid choice")