# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen
from random import choice

color_list = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

# initialize turtle and screen
tom = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("snow")

# set turtle states
tom.speed(0)

# initialize preferred turtle start position
tom_x = -380
tom_y = -350


# function to return turtle to start point
def reset_turtle():
    tom.pu()
    tom.setpos(tom_x, tom_y)


# move turtle to preferred start position
reset_turtle()


def move_turtle(grid_x, spacing):
    for _ in range(grid_x):
        new_color = choice(color_list)
        tom.dot(10, new_color)
        tom.pu()
        tom.forward(spacing)
        tom.pd()


def draw_hirsch(grid_y):
    y_cor = tom_y
    for _ in range(grid_y):
        move_turtle(51, 15)
        reset_turtle()
        y_cor += 15
        tom.sety(y_cor)
    tom.hideturtle()


draw_hirsch(50)

screen.exitonclick()
