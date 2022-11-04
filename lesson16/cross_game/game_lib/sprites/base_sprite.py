from turtle import Turtle
from abc import ABCMeta, abstractmethod


class Sprite(Turtle, metaclass=ABCMeta):
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()

    @abstractmethod
    def move(self): pass
