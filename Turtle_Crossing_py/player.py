from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player class that inherits from the Turtle class

    Args:
        Turtle (class): Python turtle class
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)  # change heading to face north
        self.start_position()

    def start_position(self):
        """Resets the turtle to the starting position"""
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Moves the turtle up by MOVE_DISTANCE"""
        self.forward(MOVE_DISTANCE)
