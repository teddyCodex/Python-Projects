from turtle import Turtle
from random import randint


# create Food class to inherit from Turtle class
class Food(Turtle):
    # initialize food class with Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")  # change shape of food
        self.pu()  # penup to prevent drawing
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # adjust size by 40%
        self.color("snow")  # change food color
        self.speed(0)
        self.new_food()

    def new_food(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)  # spawn at a random point in the screen
