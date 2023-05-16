from turtle import Screen
from snake import Snake
import time

EASY = 0.5
MEDIUM = 0.3
HARD = 0.1

screen = Screen()  # initialize new screen
screen.setup(width=600, height=600)
screen.bgcolor("black")  # change background color of screen to black
screen.title("Snake Game")  # add title name to screen
difficulty = screen.textinput("Choose Difficulty", "        Easy-Medium-Hard: ").lower()
screen.tracer(0)  # screen animation control. 0 =off, 1 = on

snake = Snake(3)  # initialize a new snake instance


screen.listen()  # listen for input
# various input options - these represent keyboard arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_active = True  # flag to control game active state

# create infinite loop to keep the snake in motion
while game_active:
    # update(refresh) the screen here (after the loop below has fully run instead of each time the loop iterates)
    screen.update()

    if difficulty == "easy":
        time.sleep(EASY)
    elif difficulty == "hard":
        time.sleep(HARD)
    else:
        time.sleep(MEDIUM)
    # move the snake
    snake.move_snake()


screen.exitonclick()  # exit the screen on click
