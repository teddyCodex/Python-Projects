from gui_manager import UserInterface


def start_program():
    gui = UserInterface()
    gui.splash_screen()
    gui.operations()
    gui.screen.mainloop()


if __name__ == "__main__":
    start_program()
