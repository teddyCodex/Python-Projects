from turtle import Turtle, Screen
from contact_book import Contact_book
import time

GREETING = "Welcome!"
GREETING_FONT = ("Lato", 24, "bold")
OPERATIONS_TEXT = "Select an operation\n\n1  to  Add a contact\n2  to  Delete a contact\n3  to  Update a contact\n4  to  Search contacts\n5  to  View all\n6  to  Exit"
OPERATIONS_FONT = ("Lato", 18, "normal")


class UserInterface:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Contact Manager")
        self.screen.bgcolor("#1e1e1e")
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color("snow")
        self.contact_book = Contact_book(self)

    def add_contact_handler(self):
        title_prompt = "Add a contact"
        self.turtle.clear()
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        last_name = self.screen.textinput(title_prompt, "Contact last name")
        address = self.screen.textinput(title_prompt, "Contact Address")
        phone_number = self.screen.textinput(title_prompt, "Contact Phone Number")
        self.contact_book.add_contact(first_name, last_name, address, phone_number)

    def delete_contact_handler(self):
        title_prompt = "Delete a contact"
        self.turtle.clear()
        contact_info = self.retrieve_contact_handler(title_prompt=title_prompt)
        if type(self.reformat_contact_info(contact_info)) == str:
            if (
                self.screen.textinput(
                    "Confirm Delete Action",
                    f"Confirm Delete (Y/N):\n{self.reformat_contact_info(contact_info)}",
                ).lower()
                == "y"
            ):
                self.contact_book.delete_contact(contact_info["name"])
            else:
                self.turtle.clear()
                self.operations()

    def confirm_delete(self, full_name):
        self.screen.listen()
        self.screen.onkey(self.contact_book.delete_contact(full_name=full_name), "y")

    def update_contact_handler(self):
        title_prompt = "Update a contact"
        self.turtle.clear()
        contact_info = self.retrieve_contact_handler(title_prompt=title_prompt)
        if type(self.reformat_contact_info(contact_info)) == str:
            if (
                self.screen.textinput(
                    title_prompt,
                    f"Update this contact? (Y/N)\n{self.reformat_contact_info(contact_info)}",
                ).lower()
                == "y"
            ):
                first_name = self.screen.textinput(
                    title_prompt, "Contact first name (leave blank if no change)"
                )
                last_name = self.screen.textinput(
                    title_prompt, "Contact last name (leave blank if no change)"
                )
                address = self.screen.textinput(
                    title_prompt, "Contact Address (leave blank if no change)"
                )
                phone_number = self.screen.textinput(
                    title_prompt, "Contact Phone Number (leave blank if no change)"
                )
                self.contact_book.update_contact(
                    contact_info["name"], first_name, last_name, address, phone_number
                )
            else:
                self.turtle.clear()
                self.operations()

    def retrieve_contact_handler(self, title_prompt):
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        last_name = self.screen.textinput(title_prompt, "Contact last name")
        contact_info = self.contact_book.retrieve_contact(first_name, last_name)
        return contact_info

    def reformat_contact_info(self, dictionary):
        contact_info = dictionary
        if (
            self.contact_book.format_contact_details(dictionary=contact_info)
            == "Contact not found."
        ):
            self.turtle.write(
                self.contact_book.format_contact_details(dictionary=contact_info),
                align="center",
                font=OPERATIONS_FONT,
            )
            time.sleep(1.5)
            self.turtle.clear()
            self.operations()
        else:
            details = ""
            for i in self.contact_book.format_contact_details(dictionary=contact_info):
                details += f"{i}\n"
            return details

    def exit_screen(self):
        self.screen.exitonclick()

    def splash_screen(self):
        self.turtle.write(f"{GREETING}", align="center", font=GREETING_FONT)
        time.sleep(2)
        self.turtle.clear()

    def operations(self):
        self.screen.listen()
        self.screen.onkey(self.add_contact_handler, "1")
        self.screen.onkey(self.delete_contact_handler, "2")
        self.screen.onkey(self.update_contact_handler, "3")
        self.turtle.write(OPERATIONS_TEXT, align="center", font=OPERATIONS_FONT)
