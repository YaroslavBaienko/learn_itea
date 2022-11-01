from turtle import *
from abc import ABCMeta, abstractmethod


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        Turtle.__init__(self, shape='circle')

