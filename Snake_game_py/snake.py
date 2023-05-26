from turtle import Turtle

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        # turtle starting position
        self.x_cor = 0
        self.y_cor = 0
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
        self.snake = Turtle("square")
        # change this snake segment instance color to white
        self.snake.color("snow")
        # raise pen to prevent drawing
        self.snake.pu()
        # adjust snake size
        self.snake.shapesize(stretch_len=0.9, stretch_wid=0.9)
        # move this snake segment to the coordinates defined at the variables
        self.snake.goto(position)
        # append this segment to the list of snake segments
        self.snake_segments.append(self.snake)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(-1000, -1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

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
        self.snake_head.fd(20)

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
