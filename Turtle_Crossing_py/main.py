import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("azure")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")  # event listener for player movement


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect player collision with car
    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle reaches the other side
    if player.ycor() > 290:
        player.start_position()  # return turtle to start position
        car_manager.increase_speed()  # increases car speed
        scoreboard.level += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
