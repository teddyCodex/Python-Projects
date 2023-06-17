# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen
from random import choice

color_list = [
    (21, 14, 9),
    (11, 32, 23),
    (9, 26, 40),
    (26, 108, 142),
    (138, 87, 42),
    (209, 153, 88),
    (43, 121, 93),
    (19, 90, 66),
    (30, 190, 160),
    (85, 238, 218),
    (22, 183, 200),
    (14, 84, 102),
    (95, 193, 171),
    (27, 43, 139),
    (9, 5, 7),
    (194, 134, 38),
    (74, 179, 237),
    (237, 204, 83),
    (64, 100, 229),
    (129, 39, 16),
    (81, 68, 36),
    (158, 243, 228),
    (236, 89, 41),
    (48, 237, 248),
    (147, 169, 253),
    (4, 248, 244),
    (162, 217, 254),
    (218, 213, 167),
    (4, 243, 248),
    (45, 48, 223),
]

# initialize turtle and screen
tom = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("snow")

# set turtle states
tom.speed(0)

# initialize preferred turtle start position
tom_x = -360
tom_y = -330


# function to return turtle to start point
def reset_turtle():
    tom.hideturtle()
    tom.pu()
    tom.setpos(tom_x, tom_y)


# move turtle to preferred start position
reset_turtle()


def move_turtle(grid_x, spacing):
    for _ in range(grid_x):
        new_color = choice(color_list)
        tom.dot(50, new_color)
        tom.pu()
        tom.forward(spacing)
        tom.pd()


def draw_hirst(grid_y):
    y_cor = tom_y
    for _ in range(grid_y):
        move_turtle(13, 60)
        reset_turtle()
        y_cor += 60
        tom.sety(y_cor)
    tom.hideturtle()


draw_hirst(12)

screen.exitonclick()
