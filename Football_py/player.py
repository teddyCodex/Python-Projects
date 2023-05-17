from turtle import Turtle

north_player_positions = [
    (0, 400),  # GK
    (100, 300),  # LCB
    (-100, 300),  # RCB
    (300, 250),  # LWB
    (-300, 250),  # RWB
    (120, 200),  # LDM
    (-120, 200),  # RDM
    (0, 100),  # CAM
    (0, 50),  # ST
    (250, 50),  # LW
    (-250, 50),  # RW
]
south_player_positions = [
    (0, -400),  # GK
    (100, -300),  # LCB
    (-100, -300),  # RCB
    (300, -250),  # LWB
    (-300, -250),  # RWB
    (0, -200),  # CDM
    (120, -150),  # LM
    (-120, -150),  # RM
    (0, -100),  # CAM
    (50, -50),  # ST
    (-50, -50),  # ST
]


class Player:
    def __init__(self) -> None:
        self.north_players_list = []  # Initialize an empty list to store the players
        self.south_players_list = []  # Initialize an empty list to store the players
        self.create_players()

    def create_players(self):
        self.north_players()
        self.south_players()

    def north_players(self):
        for position in north_player_positions:
            player = Turtle("turtle")
            player.speed(0)
            player.color("black")
            player.hideturtle()
            player.penup()
            player.goto(-400, 0)
            player.seth(270)
            player.showturtle()
            player.goto(position)
            self.north_players_list.append(player)  # Add the player to the list

    def south_players(self):
        for position in south_player_positions:
            player = Turtle("turtle")
            player.speed(0)
            player.color("purple")
            player.hideturtle()
            player.penup()
            player.goto(-400, 0)
            player.seth(90)
            player.showturtle()
            player.goto(position)
            self.south_players_list.append(player)  # Add the player to the list
