from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Place your bet", prompt="Which turtle will win? Enter a color: "
)

turtle_colors = ["red", "orange", "brown", "green", "blue", "purple"]

turtles = []

# starting positions
x_cor = -230
y_cor = -100

for i in turtle_colors:
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(i)
    turtle.goto(x=x_cor, y=y_cor)
    y_cor += 35
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won!! The {winner_color} turtle won the race!")
            else:
                print(f"You've lost!! The {winner_color} turtle won the race!")
        turtle.forward(randint(2, 10))

screen.exitonclick()
