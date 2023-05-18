from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

snake = Snake()  # initialize a new snake instance passing length as an argument
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()

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

    # detect collision with food
    if snake.snake_segments[0].distance(food) < 15:
        scoreboard.update_score()
        scoreboard.display_score()
        snake.extend_snake()
        food.new_food()

    # detect collision with wall
    if (
        snake.snake_segments[0].xcor() > 280
        or snake.snake_segments[0].xcor() < -280
        or snake.snake_segments[0].ycor() > 280
        or snake.snake_segments[0].ycor() < -280
    ):
        scoreboard.game_over()
        game_active = False  # end the game


screen.exitonclick()  # exit the screen on click
