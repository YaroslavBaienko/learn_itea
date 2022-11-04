from turtle import Turtle

from cross_game.settings.game_settings import FONT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.color('white')

    def update_scoreboard(self, player_name: str):
        self.clear()
        self.goto(-180, 200)
        self.write(arg=f"Player: {player_name}\nLevel: {self.current_level}", align="center", font=FONT)
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align="center", font=FONT)
