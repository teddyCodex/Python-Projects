import ast
import time
from turtle import Turtle, Screen

LOADING_TEXT = "Loading your Contact book..."
LOADING_TEXT_FONT = ("Trebuchet MS", 20, "bold")

OPERATIONS_TEXT = "Select an operation\n\n1 - Add contact record\n2 - Delete contact record\n3 - Update contact record\n4 - Search contact record\n5 - View all contacts\n6 - Exit"
OPERATIONS_TEXT_FONT = ("Trebuchet MS", 18, "normal")

FINE_PRINT = ("Monaco", 14, "normal")


class Contact_book(Turtle):
    def __init__(self, shape: str = "classic"):
        super().__init__(shape)
        self.screen = Screen()
        self.hideturtle()
        self.color("azure")
        self.penup()
        self.load_screen()
        time.sleep(1)
        self.operations()

    def load_screen(self):
        self.clear()
        self.write(LOADING_TEXT, align="center", font=LOADING_TEXT_FONT)

    def operations(self):
        """Function that handles the various user operations"""
        self.clear()
        self.screen.listen()
        self.screen.onkey(self.add_contact, "1")
        self.screen.onkey(self.delete_contact, "2")
        self.screen.onkey(self.update_contact, "3")
        self.screen.onkey(self.search_contact, "4")
        self.screen.onkey(self.view_all_contacts, "5")
        self.screen.onkey(self.exit_program, "6")
        self.goto(0, -50)  # adjusting content to appear central
        self.write(OPERATIONS_TEXT, align="center", font=OPERATIONS_TEXT_FONT)

    def add_contact(self):
        """Function that adds a contact to the contact book"""

        contact = {}  # dictionary to hold the contact information
        title_prompt = "Add a contact"
        self.clear()

        # collect information from the user
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        if first_name == None:
            self.clear()
            self.operations()
        else:
            last_name = self.screen.textinput(title_prompt, "Contact last name")
            address = self.screen.textinput(title_prompt, "Contact Address")
            phone_number = self.screen.textinput(title_prompt, "Contact Phone Number")
            self.clear()

            # check if there is no name input and return user home if true
            if first_name == "" and last_name == "":
                self.pu()
                self.write(
                    "Contact names not provided",
                    align="center",
                    font=OPERATIONS_TEXT_FONT,
                )
                time.sleep(1.5)
                self.clear()
                self.operations()
            else:
                # add contact as a dictionary to the dictionary initialized above
                full_name = f"{first_name} {last_name}".title()
                contact[full_name] = {
                    "name": full_name,
                    "address": address,
                    "phone_number": phone_number,
                }
                # write contents of the dictionary to the contacts.txt file
                with open("contacts.txt", mode="a") as file:
                    file.write(str(contact))
                    file.write("\n")
                self.home()
                self.write(
                    "Contact Added!",
                    align="center",
                    font=OPERATIONS_TEXT_FONT,
                )
                time.sleep(1.5)
                self.clear()
                self.operations()  # return home

    def collect_info(self, title_prompt):
        """Function that collects info from the user

        Args:
            title_prompt (str): prompt to display at the top of the dialog box

        Returns:
            str: concatenated first name and last name
        """
        error_txt = "Error!\nPlease provide first and last names"
        first_name = self.screen.textinput(title_prompt, "Contact first name")
        last_name = self.screen.textinput(title_prompt, "Contact last name")
        if first_name == "" or last_name == "":
            self.clear()
            self.home()
            self.write(error_txt, align="center", font=OPERATIONS_TEXT_FONT)
            time.sleep(1.5)
            self.operations()
        else:
            full_name = f"{first_name} {last_name}".title()
            return full_name

    def delete_contact(self):
        """Function that deletes a contact from the contact book"""
        title_prompt = "Delete a contact"
        self.clear()
        # collect full name from the user
        full_name = self.collect_info(title_prompt=title_prompt)
        # retrieve a list of contacts - this should (ideally) provide a list of dictionaries
        list_of_contacts = self.retrieve_and_parse_contacts()
        # if the list is empty, notify the user and take them back home
        if list_of_contacts is None:
            self.clear()
            self.write(
                "No Contacts Found!",
                align="center",
                font=OPERATIONS_TEXT_FONT,
            )
            time.sleep(1.5)
            self.operations()
        else:
            # loop through the list of dictionaries and check if the full name is equal to the dictionary key in current iteration
            for i in list_of_contacts:
                if full_name == list(i.keys())[0]:
                    self.clear()
                    # confirm delete action
                    contact_to_delete = self.format_contact_info(i[full_name])
                    if (
                        self.screen.textinput(
                            "Confirm Delete Action",
                            f"Confirm Delete (Y/N)\n\n{contact_to_delete}",
                        ).lower()
                        == "y"
                    ):
                        # remove the dictionary from the list of dictionaries
                        list_of_contacts.remove(i)
                        self.home()
                        self.write(
                            "Contact Deleted!",
                            align="center",
                            font=OPERATIONS_TEXT_FONT,
                        )
                        time.sleep(1.5)
                        self.clear()
                        self.operations()
                    else:
                        # if user enters N or any other action, return home
                        self.clear()
                        self.operations()
            # update the contacts.txt file with the updated list of dictionaries
            self.update_contacts_file(list_of_contacts)

    def update_contact(self):
        """Function that updates a contact in the contact book"""
        title_prompt = "Update a contact"
        self.clear()
        full_name = self.collect_info(
            title_prompt=title_prompt
        )  # return a name collected from user
        contact_list = (
            self.retrieve_and_parse_contacts()
        )  # returns a list of dictionaries

        contact_to_update = None
        for contact_dict in contact_list:
            if full_name in contact_dict:
                contact_to_update = contact_dict
                formatted_contact = self.format_contact_info(
                    contact_to_update[full_name]
                )
                if (
                    self.screen.textinput(
                        title_prompt,
                        f"Update this contact? (Y/N)\n\n{formatted_contact}",
                    ).lower()
                    == "y"
                ):
                    contact_list.remove(contact_to_update)

                    # this section collects updated info from the user
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

                    # this section checks if variables are empty and assigns existing values if true.
                    if first_name == "":
                        first_name = contact_dict[full_name]["name"].split()[0]
                    if last_name == "":
                        last_name = contact_dict[full_name]["name"].split()[1]
                    if address == "":
                        address = contact_dict[full_name]["address"]
                    if phone_number == "":
                        phone_number = contact_dict[full_name]["phone_number"]
                    updated_contact = {
                        f"{first_name} {last_name}".title(): {
                            "name": f"{first_name} {last_name}".title(),
                            "address": address,
                            "phone_number": phone_number,
                        }
                    }
                    contact_list.append(updated_contact)
                    self.write(
                        "Contact Updated!", align="center", font=OPERATIONS_TEXT_FONT
                    )
                    self.update_contacts_file(contact_list)
                    time.sleep(1.5)
                    self.operations()
                else:
                    self.clear()
                    self.operations()
                break
        else:
            self.clear()
            self.home()
            self.write("Contact Not Found", align="center", font=OPERATIONS_TEXT_FONT)
            time.sleep(1.5)
            self.operations()

    def search_contact(self):
        title_prompt = "Search Contacts"
        self.clear()
        user_input = self.collect_info(title_prompt=title_prompt)
        contacts_dict = self.retrieve_and_parse_contacts()
        contact_to_find = None
        for item in contacts_dict:
            if user_input in item:
                contact_to_find = item
                formatted_contact = self.format_contact_info(
                    contact_to_find[user_input]
                )
                self.clear()
                self.home()
                self.write(formatted_contact, align="center", font=OPERATIONS_TEXT_FONT)
                break
        else:
            self.home()
            self.write("Contact Not Found", align="center", font=OPERATIONS_TEXT_FONT)
            time.sleep(1.5)
            self.operations()

        self.goto(0, -250)
        self.write("Press Enter to go home.", align="center", font=FINE_PRINT)
        self.screen.listen()
        self.screen.onkey(self.operations, "Return")

    def view_all_contacts(self):
        self.clear()
        starting_x = -100  # starting x-coordinate
        starting_y = 200  # starting y-coordinate
        contacts_list = self.retrieve_and_parse_contacts()
        if contacts_list == None:
            self.write("No Contacts Found.", align="center", font=OPERATIONS_TEXT_FONT)
            time.sleep(1.5)
            self.operations()
        else:
            Formatted_contacts = []
            for item in contacts_list:
                key = list(item.keys())[0]
                Formatted_contacts.append(self.format_contact_info(item[key]))
            for item in Formatted_contacts:
                self.goto(starting_x, starting_y)  # move to new y-coordinate
                self.write(item, font=FINE_PRINT)
                starting_y -= 70  # decrease y-coordinate for next contact

            self.goto(starting_x, starting_y)
            self.write(
                "Press 'Enter' to go home",
                font=FINE_PRINT,
            )
            self.screen.listen()
            self.screen.onkey(self.operations, "Return")

    def exit_program(self):
        """Function to exit program upon user input"""
        self.clear()
        if self.screen.textinput("Exit?", "Exit Contact book? (Y/N)").lower() == "y":
            self.home()
            self.write("Exiting Program...", align="center", font=FINE_PRINT)
            time.sleep(1)
            exit()
        else:
            self.clear()
            self.operations()

    def retrieve_and_parse_contacts(self):
        """Function that retrieves all the contacts in the contacts.txt file as a list of strings
        then converts it to a list of dictionaries

        Returns:
            List: returns available contacts as a list of dictionaries
            None: if no contacts exist
        """
        with open("contacts.txt") as file:
            list_of_contacts = file.readlines()
        if list_of_contacts == []:
            return None
        else:
            list_of_dicts = []
            for i in list_of_contacts:
                list_of_dicts.append(ast.literal_eval(i))
            return list_of_dicts

    def format_contact_info(self, dict):
        contact_tuple = (
            "name : {}".format(dict["name"]),
            "address : {}".format(dict["address"]),
            "tel : {}".format(dict["phone_number"]),
        )
        contact_string = ""
        for i in contact_tuple:
            contact_string += f"{i}\n"
        return contact_string

    def update_contacts_file(self, list_of_dicts):
        """Function that updates the information in the contacts.txt file

        Args:
            list_of_dicts (dict): a list containing dictionaries containing the contact details
        """
        with open("contacts.txt", mode="w") as file:
            for i in list_of_dicts:
                file.write(str(i))
                file.write("\n")
