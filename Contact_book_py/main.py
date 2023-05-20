import art

print(art.logo_name)
print(art.logo)

contact_book = {}

program_active = True


# _______________________________________________________
# function to print contact details
def print_contact_details(name):
    contact = contact_book[name]
    print("\nname : {}".format(contact["name"]))
    print("address : {}".format(contact["address"]))
    print("tel : {}".format(contact["tel"]))


while program_active:
    # _______________________________________________________
    # Function to add a contact
    def add_contact():
        print("\nCREATE A NEW CONTACT")

        def add(fname, lname, address, tel):
            global contact_book
            full_name = f"{fname} {lname}".title()
            contact_book[full_name] = {
                "name": full_name,
                "address": address,
                "tel": tel,
            }
            print("\nContact saved successfully")

        while True:
            fname = input("First Name: ").lower()
            lname = input("Last Name: ").lower()
            address = input("Address: ").lower()
            tel = input("Telephone: ")
            add(fname, lname, address, tel)

            if input("Add another contact? ('y' or 'n'): ").lower() == "n":
                break

    # _______________________________________________________
    # Function to delete a contact
    def del_contact():
        def delete(name):
            print_contact_details(name)
            if input("\nConfirm delete ('y' or 'n'): ").lower() == "y":
                del contact_book[name]
                print("\nContact deleted successfully")
                # print(contact_book) # test code

        while True:
            print("\nDELETE A CONTACT")
            fname = input("First Name: ").lower()
            lname = input("Last Name: ").lower()
            full_name = f"{fname} {lname}".title()
            delete(full_name)

            if input("Delete another contact? ('y' or 'n'): ").lower() == "n":
                break

    # _______________________________________________________
    # Function to update a contact
    def update_contact():
        def update(name):
            global contact_book
            print_contact_details(name)
            new_name = input("Enter new name: ")
            new_address = input("Enter new address: ")
            new_tel = input("Enter new tel: ")
            contact_book[name] = {
                "name": new_name,
                "address": new_address,
                "tel": new_tel,
            }
            print("\nContact updated successfully")

        while True:
            print("\nUPDATE A CONTACT")
            fname = input("First Name: ").lower()
            lname = input("Last Name: ").lower()
            full_name = f"{fname} {lname}".title()
            update(full_name)

            if input("Update another contact? ('y' or 'n'): ").lower() == "n":
                break

    # _______________________________________________________
    # Function to view a contact
    def view_contact():
        while True:
            print("\nVIEW A CONTACT")
            fname = input("First Name: ").lower()
            lname = input("Last Name: ").lower()
            full_name = f"{fname} {lname}".title()
            print_contact_details(full_name)

            if input("\nView another contact? ('y' or 'n'): ").lower() == "n":
                break

    # _______________________________________________________
    # Function to view all contacts
    def view_all():
        print("\nVIEWING ALL CONTACT\n")
        for name in contact_book:
            print_contact_details(name)

    # _______________________________________________________
    # Function to exit the program
    def exit_program():
        exit()

    # _______________________________________________________
    # User operations on the contact book
    print("\n")
    operations = {
        "1": add_contact,
        "2": del_contact,
        "3": update_contact,
        "4": view_contact,
        "5": view_all,
        "6": exit,
    }

    print(
        "1 to Add a contact\n2 to Delete contact\n3 to Update a contact\n4 to View a contact\n5 to View all\n6 to exit"
    )
    user_action = input("\nSelect an action: ")
    operations[user_action]()
