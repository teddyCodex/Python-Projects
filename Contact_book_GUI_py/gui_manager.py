from turtle import Turtle, Screen
from contact_book import Contact_book
import time

# Constants for the UI
GREETING = "Welcome!"
GREETING_FONT = ("Lato", 24, "bold")
OPERATIONS_TEXT = "Select an operation\n\n1  to  Add a contact\n2  to  Delete a contact\n3  to  Update a contact\n4  to  Search contacts\n5  to  View all contacts\n6  to  Exit"
OPERATIONS_FONT = ("Lato", 18, "normal")


class UserInterface:
    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.setup(width=800, height=800)
        self.screen.title("Contact Manager")
        self.screen.bgcolor("#1e1e1e")
        # Set up the turtle for drawing
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color("snow")
        # Create an instance of the contact book
        self.contact_book = Contact_book(self)

    def add_contact_handler(self):
        """
        Handler for adding a contact. This will take the user's input and pass it to the
        add_contact function in the Contact_book class.
        """
        title_prompt = "Add a contact"
        self.turtle.clear()
        # Get contact details from the user
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        last_name = self.screen.textinput(title_prompt, "Contact last name")
        address = self.screen.textinput(title_prompt, "Contact Address")
        phone_number = self.screen.textinput(title_prompt, "Contact Phone Number")
        self.contact_book.add_contact(first_name, last_name, address, phone_number)

    def delete_contact_handler(self):
        """
        Handler for deleting a contact. This will get the contact's information from the user
        and pass it to the delete_contact function in the Contact_book class.
        """
        title_prompt = "Delete a contact"
        self.turtle.clear()
        # If the contact was found, confirm the delete operation with the user
        contact_info = self.retrieve_contact_handler(title_prompt=title_prompt)
        if self.reformat_contact_info(contact_info) != None:
            if (
                self.screen.textinput(
                    "Confirm Delete Action",
                    f"Confirm Delete (Y/N):\n{self.reformat_contact_info(contact_info)}",
                ).lower()
                == "y"
            ):
                self.contact_book.delete_contact(contact_info["name"])
            else:
                # If the user didn't confirm, clear the screen and return to the main menu
                self.turtle.clear()
                self.operations()

    def update_contact_handler(self):
        """
        Handler for updating a contact. This will get the contact's information from the user
        and pass it to the update_contact function in the Contact_book class.
        """
        title_prompt = "Update a contact"
        self.turtle.clear()
        contact_info = self.retrieve_contact_handler(title_prompt=title_prompt)
        if self.reformat_contact_info(contact_info) != None:
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

    def search_contacts_handler(self):
        """
        Handler for searching for a contact.
        Utilizes the retrieve contact function to trigger the
        search_contact function from contact_book.py
        """
        title_prompt = "Search Contacts"
        self.turtle.clear()
        contact_info = self.retrieve_contact_handler(title_prompt=title_prompt)
        formatted_contact_info = self.reformat_contact_info(contact_info)
        if formatted_contact_info != None:
            self.turtle.clear()
            self.turtle.write(
                f"Contact Found\n\n{formatted_contact_info}\n\nPress 'Enter' to go home",
                align="center",
                font=OPERATIONS_FONT,
            )
        self.screen.listen()
        self.screen.onkey(self.operations, "Return")

    def view_all_contacts(self):
        """Function to display all saved contacts"""
        self.turtle.clear()
        self.turtle.pu()

        current_x = -100  # starting x-coordinate
        current_y = 200  # starting y-coordinate

        # check if the contact book is empty
        if self.contact_book.contacts == {}:
            self.turtle.write(
                "No Contacts Found", align="center", font=("Lato", 15, "normal")
            )
            time.sleep(1.5)
            self.operations()
        else:
            for i in self.contact_book.contacts:
                sub_dict = self.contact_book.contacts[i]
                sub_dict_tuple = self.contact_book.format_contact_details(sub_dict)
                details = ""
                for j in sub_dict_tuple:
                    details += f"{j}\n"
                self.turtle.goto(current_x, current_y)  # move to new y-coordinate
                self.turtle.write(details, font=("Lato", 15, "normal"))
                current_y -= 70  # decrease y-coordinate for next contact

            self.turtle.goto(current_x, current_y)
            self.turtle.write(
                "Press 'Enter' to go home",
                font=("Lato", 14, "bold"),
            )
            self.screen.listen()
            self.screen.onkey(self.operations, "Return")

    def retrieve_contact_handler(self, title_prompt):
        """Function to retrieve contact info

        Args:
            title_prompt (str): Title to appear at the top of the dialog box

        Returns:
            dictionary: returns a dictionary containing the contact details.
            returns None if contact is not found
        """
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        last_name = self.screen.textinput(title_prompt, "Contact last name")
        contact_info = self.contact_book.search_contacts(first_name, last_name)
        return contact_info

    def reformat_contact_info(self, dictionary):
        """Function that converts a dictionary of contact_info to a string

        Args:
            dictionary (dictionary): a dictionary containing the contact details.

        Returns:
            string: a string containing the data from the dictionary
        """
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

    def splash_screen(self):
        """Initial splash screen (Welcome Screen)"""
        self.turtle.write(f"{GREETING}", align="center", font=GREETING_FONT)
        time.sleep(2)
        self.turtle.clear()

    def operations(self):
        """Function that handles the various user operations"""
        self.turtle.clear()
        self.turtle.home()
        self.screen.listen()
        self.screen.onkey(self.add_contact_handler, "1")
        self.screen.onkey(self.delete_contact_handler, "2")
        self.screen.onkey(self.update_contact_handler, "3")
        self.screen.onkey(self.search_contacts_handler, "4")
        self.screen.onkey(self.view_all_contacts, "5")
        self.screen.onkey(self.exit_program, "6")
        self.turtle.write(OPERATIONS_TEXT, align="center", font=OPERATIONS_FONT)

    def exit_program(self):
        """Function to exit program upon user input"""
        self.turtle.clear()
        if self.screen.textinput("Exit?", "Exit Contact book? (Y/N)").lower() == "y":
            self.turtle.write(
                "Exiting Program...", align="center", font=OPERATIONS_FONT
            )
            time.sleep(1)
            exit()
        else:
            self.turtle.clear()
            self.operations()
