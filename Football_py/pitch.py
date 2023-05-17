from turtle import Turtle, Screen
from player import Player

PITCH_MARGIN = 30
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
SIDEBAR = 100
CROSSBAR = 200


class Pitch:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.pen = Turtle("circle")
        self.pen.color("snow")
        self.pen.hideturtle()
        self.pen.speed(0)
        self.draw_pitch_screen()

    def draw_pitch_screen(self):
        self.pitch = Screen()
        self.pitch.colormode(255)
        self.pitch.bgcolor(86, 125, 70)
        # width = 800, height = 900
        self.pitch.setup(width=self.width, height=self.height)
        self.draw_pitch_area()
        self.new_player = Player()
        self.pitch.exitonclick()

    def move_left(self, length):
        self.pen.seth(WEST)
        self.pen.fd(length)

    def move_up(self, length):
        self.pen.seth(NORTH)
        self.pen.fd(length)

    def move_right(self, length):
        self.pen.seth(EAST)
        self.pen.fd(length)

    def move_down(self, length):
        self.pen.seth(SOUTH)
        self.pen.fd(length)

    def reset(self):
        self.pen.pu()
        self.pen.home()

    def draw_pitch_area(self):
        self.draw_sidelines()
        self.draw_center_circle()
        self.draw_goalposts()

    def draw_sidelines(self):
        self.move_right((self.width / 2) - PITCH_MARGIN)
        self.move_up((self.height / 2) - PITCH_MARGIN)
        self.move_left((self.width - (PITCH_MARGIN + PITCH_MARGIN)))
        self.move_down(self.height - (PITCH_MARGIN + PITCH_MARGIN))
        self.move_right(self.width - (PITCH_MARGIN + PITCH_MARGIN))
        self.move_up((self.height / 2) - PITCH_MARGIN)
        self.move_left((self.width - (PITCH_MARGIN + PITCH_MARGIN)))
        self.reset()

    def draw_center_circle(self):
        self.pen.pd()
        self.pen.stamp()
        self.move_left(58)
        self.pen.seth(0)
        self.pen.right(90)
        self.pen.circle(58)
        self.reset()

    def draw_goalposts(self):
        self.south_post()
        self.north_post()

    def south_post(self):
        self.pen.pu()
        self.move_left(100)
        self.move_down((self.height / 2) - PITCH_MARGIN)
        self.pen.pd()
        self.move_up(SIDEBAR)
        self.move_right(CROSSBAR)
        self.move_down(SIDEBAR)
        self.reset()

    def north_post(self):
        self.pen.pu()
        self.move_left(100)
        self.move_up((self.height / 2) - PITCH_MARGIN)
        self.pen.pd()
        self.move_down(SIDEBAR)
        self.move_right(CROSSBAR)
        self.move_up(SIDEBAR)
