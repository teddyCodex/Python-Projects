from turtle import Turtle
import time

OPERATIONS_FONT = ("Lato", 18, "normal")


class Contact_book(Turtle):
    def __init__(self, user_interface):
        super().__init__()
        self.hideturtle()
        self.color("snow")
        self.contacts = {}
        self.user_interface = user_interface

    def add_contact(self, first_name, last_name, address, phone_number):
        self.clear()
        full_name = f"{first_name} {last_name}".title()
        self.contacts[full_name] = {
            "name": full_name,
            "address": address,
            "phone_number": phone_number,
        }
        self.write(
            "Contact Added!",
            align="center",
            font=OPERATIONS_FONT,
        )
        time.sleep(1)
        self.clear()
        self.user_interface.operations()

    def retrieve_contact(self, first_name, last_name):
        self.clear()
        full_name = f"{first_name} {last_name}".title()
        if full_name in self.contacts:
            return self.contacts[full_name]
        else:
            return None

    def delete_contact(self, full_name):
        self.clear()
        del self.contacts[full_name]
        self.write(
            "Contact Deleted!",
            align="center",
            font=OPERATIONS_FONT,
        )
        time.sleep(1.5)
        self.clear()
        self.user_interface.operations()

    def update_contact(
        self, contact_name, first_name, last_name, address, phone_number
    ):
        if first_name == "":
            first_name = self.contacts[contact_name]["name"].split()[0]
        if last_name == "":
            last_name = self.contacts[contact_name]["name"].split()[1]
        if address == "":
            address = self.contacts[contact_name]["address"]
        if phone_number == "":
            phone_number = self.contacts[contact_name]["phone_number"]

        full_name = f"{first_name} {last_name}"
        self.contacts[full_name] = {
            "name": full_name,
            "address": address,
            "phone_number": phone_number,
        }
        self.clear()
        self.write(
            "Contact Updated!",
            align="center",
            font=OPERATIONS_FONT,
        )
        time.sleep(1.5)
        self.clear()
        self.user_interface.operations()

    def format_contact_details(self, dictionary):
        if dictionary is not None:
            return (
                "name : {}".format(dictionary["name"]),
                "address : {}".format(dictionary["address"]),
                "tel : {}".format(dictionary["phone_number"]),
            )
        else:
            return "Contact not found."


# def print_contact_details(name):
#     contact = contacts[name]
#     print("\nname : {}".format(contact["name"]))
#     print("address : {}".format(contact["address"]))
#     print("tel : {}".format(contact["tel"]))


#     # _______________________________________________________
#     # Function to update a contact
#     def update_contact():
#         def update(name):
#             global contacts
#             print_contact_details(name)
#             new_name = input("Enter new name: ")
#             new_address = input("Enter new address: ")
#             new_tel = input("Enter new tel: ")
#             contacts[name] = {
#                 "name": new_name,
#                 "address": new_address,
#                 "tel": new_tel,
#             }
#             print("\nContact updated successfully")

#         while True:
#             print("\nUPDATE A CONTACT")
#             fname = input("First Name: ").lower()
#             lname = input("Last Name: ").lower()
#             full_name = f"{fname} {lname}".title()
#             update(full_name)

#             if input("Update another contact? ('y' or 'n'): ").lower() == "n":
#                 break

#     # _______________________________________________________
#     # Function to view a contact
#     def view_contact():
#         while True:
#             print("\nVIEW A CONTACT")
#             fname = input("First Name: ").lower()
#             lname = input("Last Name: ").lower()
#             full_name = f"{fname} {lname}".title()
#             print_contact_details(full_name)

#             if input("\nView another contact? ('y' or 'n'): ").lower() == "n":
#                 break

#     # _______________________________________________________
#     # Function to view all contacts
#     def view_all():
#         print("\nVIEWING ALL CONTACT\n")
#         for name in contacts:
#             print_contact_details(name)

#     # _______________________________________________________
#     # Function to exit the program
#     def exit_program():
#         exit()
