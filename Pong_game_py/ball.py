from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("azure")
        self.move_x = 10
        self.move_y = 10

    def move(self):
        self.penup()
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1
