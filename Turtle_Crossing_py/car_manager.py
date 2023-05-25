from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (250, 0)


class CarManager:
    def __init__(self) -> None:
        pass

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1, outline=5)
        car.penup()
        car.goto(STARTING_POSITION)
