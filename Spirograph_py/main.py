from turtle import Turtle, Screen, forward, left, right, back
from random import choice, randint

screen = Screen()
screen.colormode(255)


tim = Turtle()
tim.speed(0)
tim.hideturtle()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spiro(spacing):
    for _ in range(int(360 / spacing)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + spacing)


draw_spiro(5)

screen.exitonclick()
