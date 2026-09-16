# contacts = [
#     {
#         "name": "Tarun",
#         "phone": "9876543210",
#         "email": "tarun@example.com"
#     }
# ]

# #add
# def add_contact():
#     name = input("Enter name: ")
#     phone = input("Enter phone: ")
#     email = input("Enter email: ")
#     if not phone:
#         print("Phone number cannot be empty")
#         return
#     if not email:
#         print("Email cannot be empty")
#         return
#     for contact in contacts:
#         if contact["name"] == name:
#             print("Contact already exists")
#             return         
#     new_contact = {
#         "name": name,
#         "phone": phone,
#         "email": email
#     }     
#     contacts.append(new_contact)
#     print("Added !")   

# # delete
# def delete_contact():
#     name = input("Enter name to delete: ")
#     for contact in contacts:
#         if contact["name"] == name:
#             contacts.remove(contact)
#             print("Deleted !")
#             return
#     else:
#         print("Not Found")
        
# # search
# def search_contact():
#     name = input("Enter name to search: ")  
#     for contact in contacts:
#         if contact["name"] == name:
#             print("Found !")
#             print(contact)
#             return
#     print("Not Found")    

# # update
# def update_contact():
#     name = input("Enter name to update: ") 
#     for contact in contacts:
#         if contact["name"] == name:
#             new_phone = input("New Phone: ")
#             new_email = input("New email: ")
#             if not new_phone:
#                 print("Phone number cannot be empty")
#                 return
#             if not new_email:
#                 print("Email cannot be empty")
#                 return
#             contact["phone"] = new_phone 
#             contact["email"] = new_email 
#             print("Updated") 
#             return   
#     print("Not found")
                
# # list
# def list_contacts():
#     for contact in contacts:
#         print(contact)
        
        

# using class
class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactManager:

    def __init__(self):
        self.contacts = [
            Contact("Tarun", "9876543210", "tarun@example.com")
        ]

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        if not phone:
            print("Phone number cannot be empty")
            return

        if not email:
            print("Email cannot be empty")
            return

        for contact in self.contacts:
            if contact.name == name:
                print("Contact already exists")
                return

        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)

        print("Added !")

    def delete_contact(self):
        name = input("Enter name to delete: ")

        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Deleted !")
                return

        print("Not Found")

    def search_contact(self):
        name = input("Enter name to search: ")

        for contact in self.contacts:
            if contact.name == name:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                return

        print("Not Found")

    def update_contact(self):
        name = input("Enter name to update: ")

        for contact in self.contacts:
            if contact.name == name:

                new_phone = input("New Phone: ")
                new_email = input("New Email: ")

                if not new_phone:
                    print("Phone number cannot be empty")
                    return

                if not new_email:
                    print("Email cannot be empty")
                    return

                contact.phone = new_phone
                contact.email = new_email

                print("Updated")
                return

        print("Not Found")

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print()        