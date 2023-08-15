from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for char in range(nr_letters)]
        + [random.choice(symbols) for char in range(nr_symbols)]
        + [random.choice(numbers) for char in range(nr_numbers)]
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_record():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(
            message="Please fill all fields!", parent=mainframe, icon="error"
        )
    else:
        confirmation = messagebox.askokcancel(
            message=f"Save this record?:\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}",
            icon="question",
            title="Add Record",
            parent=mainframe,
        )

        if confirmation:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Ubuntu Password Manager")
root.config(padx=30, pady=30, bg="dim gray")
root.resizable(False, False)

s = ttk.Style()
s.configure(
    "border.TFrame",
    background="orangered",
    borderwidth=5,
    relief="raised",
)


mainframe = ttk.Frame(root, padding="40 40", style="border.TFrame")
mainframe.grid(column=0, row=0)


canvas = Canvas(mainframe, width=200, height=200)
logo_img = PhotoImage(file="logo.png")

# tuple represents position of img on canvas
canvas.create_image((140, 100), image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = ttk.Label(mainframe, text="Website:")
website_label.grid(row=1, column=0)
email_label = ttk.Label(mainframe, text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = ttk.Label(mainframe, text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = ttk.Entry(mainframe, width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = ttk.Entry(mainframe, width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "someone@example.com")
password_entry = ttk.Entry(mainframe, width=22)
password_entry.grid(row=3, column=1)

# Buttons
password_btn = ttk.Button(
    mainframe, text="Generate Password", command=generate_password
)
password_btn.grid(row=3, column=2)
add_btn = ttk.Button(mainframe, text="Add Record", width=37, command=add_record)
add_btn.grid(row=4, column=1, columnspan=2)


root.mainloop()
