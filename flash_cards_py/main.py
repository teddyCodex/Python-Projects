import tkinter as tk
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

# Access data file to extract languages. # Assuming file is in correct format
csv_file = pd.read_csv("data/de-en.csv")
data = pd.DataFrame.to_dict(csv_file, orient="records")

languages = [x.lower() for x in data[0].keys()]

LANGUAGE_TO_LEARN = languages[0]
BASE_LANGUAGE = languages[1]

word_list = [[x for x in dic.values()] for dic in data]  # list of word pair lists


def generate_new_word_pair() -> list:
    info_label.config(text="", pady=0)
    word_pair = rd.choice(word_list)
    update_flashcard(word_pair)


def flip_card(lst):
    flashcard.change_image()
    flashcard.change_card_title()
    flashcard.change_card_text(lst=lst, side=0)  # 0 represents base_language


def update_flashcard(lst):
    flashcard.reset()
    flashcard.change_card_text(lst=lst, side=1)  # 1 represents language_to_learn
    root.after(3000, flip_card, lst)


### --------------------------- UI SETUP ----------------------------- ###
root = tk.Tk()
root.title("German-English Flashcards")
root.config(padx=50, pady=30, bg=BACKGROUND_COLOR)

# Images
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
right_btn_img = tk.PhotoImage(file="images/right.png")
wrong_btn_img = tk.PhotoImage(file="images/wrong.png")


class Flashcard(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_image = self.create_image(400, 263, image=card_front)
        self.card_title = self.create_text(
            400,
            150,
            text=LANGUAGE_TO_LEARN.title(),
            fill="black",
            font=("Didot", 40, "italic"),
        )
        self.card_text = self.create_text(
            400,
            263,
            text=word_list[word_list.index(rd.choice(word_list))][0],
            fill="black",
            font=("Didot", 70, "bold"),
        )

    def reset(self):
        self.itemconfig(self.canvas_image, image=card_front)
        self.itemconfig(self.card_title, text=LANGUAGE_TO_LEARN.title(), fill="black")

    def change_image(self):
        self.itemconfig(self.canvas_image, image=card_back)

    def change_card_title(self):
        self.itemconfig(self.card_title, text=BASE_LANGUAGE.title(), fill="white")

    def change_card_text(self, lst, side):
        if side:
            self.itemconfig(self.card_text, text=lst[0], fill="black")
        else:
            self.itemconfig(self.card_text, text=lst[1], fill="white")


# Create new flashcard instance
flashcard = Flashcard(root)
flashcard.grid(row=0, columnspan=2)


# Buttons
right_button = tk.Button(
    image=right_btn_img, highlightthickness=0, bd=0, command=generate_new_word_pair
)
right_button.grid(row=1, column=1)
wrong_button = tk.Button(
    image=wrong_btn_img, highlightthickness=0, bd=0, command=generate_new_word_pair
)
wrong_button.grid(row=1, column=0)

# Info Label
info_label = tk.Label(
    text="Click any of the buttons to start",
    bg=BACKGROUND_COLOR,
    fg="black",
    font=("Didot", 20, "bold"),
    pady=30,
)
info_label.grid(columnspan=2)

root.mainloop()
