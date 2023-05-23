from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("powderblue")
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        self.penup()
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.ball_speed *= 0.6

    def reset_ball(self):
        self.home()
        self.ball_speed = 0.1
        self.bounce_x()
