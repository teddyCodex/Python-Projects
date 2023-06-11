from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color("#434654")
        self.goto(200, 265)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(
            f"{self.score} of 50 States Guessed",
            align="center",
            font=("Futura", 22, "bold"),
        )

    def update_score(self):
        self.score += 1
        self.display_score()
