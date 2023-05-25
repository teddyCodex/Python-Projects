from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """This function generates a random number when called.
        If random number is 1, a turtle object is created with the added attributes
        """
        random_number = random.randint(1, 6)
        if random_number == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1, outline=5)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        """This function moves all the cars in the list of cars"""
        for car in self.cars:
            car.back(self.car_speed)

    def increase_speed(self):
        """This function increases the car speed by MOVE_INCREMENT"""
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)
