from contacts import ContactManager
manager = ContactManager()

while True:

    print("\n1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.delete_contact()

    elif choice == "3":
        manager.search_contact()

    elif choice == "4":
        manager.update_contact()

    elif choice == "5":
        manager.list_contacts()

    elif choice == "6":
        break

    else:
        print("Invalid choice")