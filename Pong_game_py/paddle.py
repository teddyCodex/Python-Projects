from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("azure")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5, outline=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
