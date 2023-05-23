from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    scoreboard.draw_line()
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect wall collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 400:
        scoreboard.l_point()
        time.sleep(1)
        ball.reset_ball()

    # detect left paddle miss
    if ball.xcor() < -410:
        scoreboard.r_point()
        time.sleep(0.8)
        ball.reset_ball()


screen.exitonclick()
