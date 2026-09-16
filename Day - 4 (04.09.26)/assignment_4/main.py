from contacts import add_contact, delete_contact, search_contact, update_contact, list_contacts

while True:
    print("\n1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")   
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        list_contacts()
    elif choice == "6":
        break
    else:
        print("Invalid")