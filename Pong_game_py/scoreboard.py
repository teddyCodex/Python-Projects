from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("azure")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def move(self):
        self.pd()
        self.fd(15)
        self.pu()
        self.fd(15)

    def draw_line(self):
        self.pu()
        self.pensize(5)
        self.goto(0, 280)
        self.seth(270)
        for _ in range(19):
            self.move()

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align="center", font=("Impact", 80, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align="center", font=("Impact", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
