from turtle import Turtle
import time

# contact book constants
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
        if first_name == "" and last_name == "":
            self.pu()
            self.write(
                "Contact names not provided",
                align="center",
                font=("Lato", 16, "normal"),
            )
            time.sleep(1.5)
            self.clear()
            self.user_interface.operations()
        else:
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

    def search_contacts(self, first_name, last_name):
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
