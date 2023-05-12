from turtle import Turtle, Screen, forward, left, right, back
from random import choice, randint

screen = Screen()
screen.colormode(255)


tim = Turtle()
tim.speed(0)
# tim.pensize(10)


def keep_within_bounds():
    x, y = tim.position()  # Get the turtle's current position
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    if x > screen_width / 2:  # If turtle moves to the right screen edge
        tim.setx(screen_width / 2)  # Set turtle's x-coordinate to the right edge
    elif x < -screen_width / 2:  # If turtle moves to the left screen edge
        tim.setx(-screen_width / 2)  # Set turtle's x-coordinate to the left edge

    if y > screen_height / 2:  # If turtle moves to the top screen edge
        tim.sety(screen_height / 2)  # Set turtle's y-coordinate to the top edge
    elif y < -screen_height / 2:  # If turtle moves to the bottom screen edge
        tim.sety(-screen_height / 2)  # Set turtle's y-coordinate to the bottom edge

    # turtle.ontimer(
    #     keep_within_bounds, 10
    # )  # Check turtle's position every 10 milliseconds


# Call the function to start keeping the turtle within bounds
keep_within_bounds()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spiro(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size)


draw_spiro(5)

screen.exitonclick()
