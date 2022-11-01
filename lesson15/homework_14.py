from turtle import *
from random import random, randint, choice
from time import sleep


class Window:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH_HALF = SCREEN_WIDTH // 2
    SCREEN_HEIGHT_HALF = SCREEN_HEIGHT // 2

    def __init__(self, screen_title: str = 'Window title'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.SCREEN_WIDTH, Window.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)


class Sprite(Turtle):
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()


class Figure(Sprite):
    size = 20

    def __init__(self, figure: str):
        super().__init__(figure)
        self.color(self.get_random_color())
        self.goto(self.get_random_position())
        self.showturtle()
        self.x = 0
        self.y = 0
        self.delta_x = 0
        self.delta_y = 0

    def move(self, gravity: float):
        self.x = self.xcor()
        self.y = self.ycor()
        self.goto(self.x + self.delta_x, self.y - self.delta_y)
        self.delta_y += gravity

    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        return randint(-Window.SCREEN_WIDTH_HALF, Window.SCREEN_WIDTH_HALF), randint(0, Window.SCREEN_HEIGHT_HALF)


class Game:
    __directions = (-1, 1)
    __gravity = 0.1
    __figures_qty = 0

    def __init__(self, figures_qty: int):
        Game.__figures_qty = figures_qty
        self.window = Window()
        self.figures = self.make_figures(figures_qty)

    def run(self):
        for figure in self.figures:
            figure.delta_x = 2 * choice(self.__directions)
            figure.delta_y = 2

        while True:
            for figure in self.figures:
                figure.move(Game.__gravity)
                Game.check_border(figure)
            self.window.canvas.update()
            if Game.__figures_qty < 50:
                sleep(0.0001 * Game.__figures_qty)
            self.check_collision(self.figures)

    @staticmethod
    def check_collision(figures: list[Figure]):
        for i in range(len(figures)):
            for j in range(i + 1, len(figures)):
                if figures[i].distance(figures[j]) < Figure.size:
                    figures[i].delta_x, figures[j].delta_x = figures[j].delta_x, figures[i].delta_x
                    figures[i].delta_y, figures[j].delta_y = figures[j].delta_y, figures[i].delta_y

    @staticmethod
    def check_border(figure):
        x = figure.xcor()
        y = figure.ycor()

        if y < -Window.SCREEN_HEIGHT_HALF:
            figure.delta_y = -figure.delta_y

        if x > Window.SCREEN_WIDTH_HALF or x < -Window.SCREEN_WIDTH_HALF:
            figure.delta_x = -figure.delta_x

    @staticmethod
    def make_figures(figures_qty: int):
        figures = ('turtle', 'circle', 'square', 'triangle')
        return [Figure(choice(figures)) for _ in range(figures_qty)]


if __name__ == '__main__':
    game = Game(figures_qty=10)
    game.run()
