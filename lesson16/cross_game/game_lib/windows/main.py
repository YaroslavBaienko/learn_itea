from turtle import Screen

from cross_game.settings.game_settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Window:
    def __init__(self, screen_title: str = 'Cross Turtle Game'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)
