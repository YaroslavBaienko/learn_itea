"""Base class Planet"""
from math import sin, cos

from solar_system.classes.sprite import Sprite


class Planet(Sprite):
    """Planet class"""
    def __init__(self, obj, star):
        Sprite.__init__(self)
        self.name = obj.name
        self.speed(0)
        self.shapesize(*obj.planet_size)
        self.x = 0
        self.y = 0
        self.color(obj.planet_color)
        self.up()
        self.angle = 0
        self.increase_angle = obj.increase_angle
        self.radius = obj.radius
        self.star = star

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle
