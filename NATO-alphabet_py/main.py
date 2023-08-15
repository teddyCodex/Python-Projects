import pandas, turtle
import time

pen = turtle.Turtle()
pen.color("azure")
pen.hideturtle()
screen = turtle.Screen()
screen.bgcolor("#333")
screen.setup(width=800, height=600)

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_word():
    word = screen.textinput(title="Convert a word", prompt="Enter a word")

    try:
        nato_word = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        pen.write(
            f"Only letters in the alphabets please.",
            align="center",
            font=("PT Mono", 14, "bold"),
        )
        time.sleep(2)
        pen.clear()
        generate_word()
    else:
        pen.write(
            f"{word}:\n\n{nato_word}",
            align="center",
            font=("PT Mono", 14, "bold"),
        )


generate_word()

turtle.mainloop()
