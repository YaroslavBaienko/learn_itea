from turtle import Turtle

from cross_game.settings.game_settings import FONT


class PauseLabel(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def update_pause(self):
        self.clear()
        self.color('red')
        self.write(arg=f"Player set pause", align="center", font=FONT)
