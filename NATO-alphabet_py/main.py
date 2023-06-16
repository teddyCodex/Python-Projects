import pandas, turtle

pen = turtle.Turtle()
pen.color("azure")
pen.hideturtle()
screen = turtle.Screen()
screen.bgcolor("#110011")
screen.setup(width=1000, height=600)

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

word = screen.textinput(title="Convert a word", prompt="Enter a word")

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_word = [nato_dict[letter.upper()] for letter in word]

pen.write(
    f"{word}:\n\n{nato_word}",
    align="center",
    font=("PT Mono", 14, "bold"),
)

turtle.mainloop()
