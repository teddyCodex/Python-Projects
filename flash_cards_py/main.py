import tkinter as tk
import pandas as pd
import random as rd
from pathlib import Path

BACKGROUND_COLOR = "#B1DDC6"

# check for words to learn file
# Access csv data file to extract languages and word pairs.
## Assuming file is in correct format
try:
    csv_file = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv_file = pd.read_csv("data/de-en.csv")
    data = pd.DataFrame.to_dict(csv_file, orient="records")
else:
    data = pd.DataFrame.to_dict(csv_file, orient="records")

# create a list of languages with their respective names (for display purposes)
languages = [x.lower() for x in data[0].keys()]

LANGUAGE_TO_LEARN = languages[0]
BASE_LANGUAGE = languages[1]

# create list of word pair lists
words_to_learn = [[x for x in dic.values()] for dic in data]

current_word_pair = list()


def start_btn():
    right_button.config(state=tk.NORMAL)
    wrong_button.config(state=tk.NORMAL)
    start_button.grid_forget()
    end_button.grid(columnspan=2)
    generate_new_word_pair()


def generate_new_word_pair():
    word_pair = rd.choice(words_to_learn)
    current_word_pair.append(word_pair)
    update_flashcard(word_pair)


def flip_card(lst):
    flashcard.change_image()
    flashcard.change_card_title()
    flashcard.change_card_text(lst=lst, side=0)  # 0 represents base_language


def update_flashcard(lst):
    flashcard.reset()
    flashcard.change_card_text(lst=lst, side=1)  # 1 represents language_to_learn
    root.after(3000, flip_card, lst)


def right_btn_clicked():
    words_to_learn.remove(current_word_pair[0])
    current_word_pair.pop()
    generate_new_word_pair()


def wrong_btn_clicked():
    current_word_pair.pop()
    generate_new_word_pair()


def end():
    df = pd.DataFrame(words_to_learn, columns=[LANGUAGE_TO_LEARN, BASE_LANGUAGE])
    filepath = Path("data/words_to_learn.csv")
    df.to_csv(filepath, index=False)
    quit()


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
            text="",
            fill="black",
            font=("Didot", 40, "italic"),
        )
        self.card_text = self.create_text(
            400,
            250,
            # text=words_to_learn[words_to_learn.index(rd.choice(words_to_learn))][0],
            text=f"{LANGUAGE_TO_LEARN.title()}\n     to\n{BASE_LANGUAGE.title()}",
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
    image=right_btn_img,
    highlightthickness=0,
    bd=0,
    command=right_btn_clicked,
    state=tk.DISABLED,
)
right_button.grid(row=1, column=1)
wrong_button = tk.Button(
    image=wrong_btn_img,
    highlightthickness=0,
    bd=0,
    command=wrong_btn_clicked,
    state=tk.DISABLED,
)
wrong_button.grid(row=1, column=0)

# Start
start_button = tk.Button(
    text="START", width=10, pady=10, font=("Helvetica", 30, "bold"), command=start_btn
)
start_button.grid(columnspan=2)

# End
end_button = tk.Button(
    text="END", width=10, pady=10, font=("Helvetica", 30, "bold"), command=end
)


root.mainloop()
