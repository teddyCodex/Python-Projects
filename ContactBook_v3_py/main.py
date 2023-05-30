from turtle import Screen
from contact_book import Contact_book


# screen setup
screen = Screen()
screen.setup(width=500, height=700)
screen.bgcolor("#393646")
screen.title("Contacts Manager")

# create a new contact book instance
contact_book = Contact_book()

screen.mainloop()
