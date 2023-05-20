from gui_manager import UserInterface


def start_program():
    """this function starts the contact book program"""
    gui = UserInterface()  # initialize new UI
    gui.splash_screen()  # display splash screen
    gui.operations()  # display available operations
    gui.screen.mainloop()


if __name__ == "__main__":
    start_program()
