from turtle import Turtle

MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self, snake_length) -> None:
        # turtle starting position
        self.x_cor = 0
        self.y_cor = 0
        self.snake_segments = []
        self.create_snake(snake_length)

    def create_snake(self, length):
        for i in range(length):
            # for this iteration, initialize new snake segment
            self.snake = Turtle("square")
            # change this snake segment instance color to white
            self.snake.color("snow")
            # raise pen to prevent drawing
            self.snake.pu()
            # adjust snake size
            self.snake.shapesize(stretch_len=0.9, stretch_wid=0.9)
            # move this snake segment to the coordinates defined at the variables
            self.snake.goto(x=self.x_cor, y=self.y_cor)
            # adjust the x_coordinate to move the next snake segment to desired position
            self.x_cor -= MOVE_DISTANCE
            # append this segment to the list of snake segments
            self.snake_segments.append(self.snake)

    def move_snake(self):
        # loop to iterate from the end of the list
        for index in range(len(self.snake_segments) - 1, 0, -1):
            # new x-coordinate to be the coordinate of the segment in front
            new_x = self.snake_segments[index - 1].xcor()
            # new y-coordinate to be the coordinate of the segment in front
            new_y = self.snake_segments[index - 1].ycor()
            # move this segment to the new coordinates
            self.snake_segments[index].goto(new_x, new_y)
        # after loop has run, move the first segment forward
        self.snake_segments[0].fd(MOVE_DISTANCE)

    def up(self):
        """This function checks if the snake is facing north or south.
        If True, it does nothing.
        Else, change snake heading to North
        """
        if (
            self.snake_segments[0].heading() == NORTH
            or self.snake_segments[0].heading() == SOUTH
        ):
            pass
        else:
            self.snake_segments[0].setheading(NORTH)

    def down(self):
        """This function checks if the snake is facing north or south.
        If True, it does nothing.
        Else, change snake heading to South
        """
        if (
            self.snake_segments[0].heading() == NORTH
            or self.snake_segments[0].heading() == SOUTH
        ):
            pass
        else:
            self.snake_segments[0].setheading(SOUTH)

    def left(self):
        """This function checks if the snake is facing east or west.
        If True, it does nothing.
        Else, change snake heading to West
        """
        if (
            self.snake_segments[0].heading() == EAST
            or self.snake_segments[0].heading() == WEST
        ):
            pass
        else:
            self.snake_segments[0].setheading(WEST)

    def right(self):
        """This function checks if the snake is facing east or west.
        If True, it does nothing.
        Else, change snake heading to East
        """
        if (
            self.snake_segments[0].heading() == EAST
            or self.snake_segments[0].heading() == WEST
        ):
            pass
        else:
            self.snake_segments[0].setheading(EAST)
