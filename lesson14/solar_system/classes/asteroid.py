"""Inherit class Asteroid of class Planet"""
from random import random

from solar_system.classes.planet import Planet
from solar_system.classes.planet_data import PlanetData


class Asteroid(Planet):
    """Asteroid class"""
    start_angle = 0.001
    increase_start_angle = 0.012421

    def __init__(self, star, radius):
        self.obj = PlanetData((0.1, 0.1), self.generate_color(), radius, self.increase_start_angle)
        Planet.__init__(self, self.obj, star)
        self.angle += self.start_angle
        Asteroid.start_angle += self.increase_start_angle

    @staticmethod
    def generate_color():
        return random(), random(), random()
