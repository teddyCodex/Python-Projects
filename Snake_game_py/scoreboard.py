from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Helvetica", 24, "normal")


# scoreboard class to inherit all attributes and methods of the turtle class
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0  # score variable to track user score
        with open("data.txt") as file:
            self.high_score = int(
                file.read()
            )  # reads the high score from the data.txt file
        self.color("snow")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)  # moving the scoreboard to the top of the screen

    def update_score(self):
        """function increments the score by 1"""
        self.score += 1
        self.display_score()

    def display_score(self):
        """function clears the screen then displays the current score value"""
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     """function displays the game over message and ends the game"""
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
