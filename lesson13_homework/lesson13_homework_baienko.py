from turtle import *
from math import *
import random
import time


class Planet(Turtle):
    def __init__(self, radius, planet_color, planet_size, increase_angle, name):
        Turtle.__init__(self, shape='circle')
        self.radius = radius
        self.speed(0)
        self.color(planet_color)
        self.x = 0
        self.y = 0
        self.planet_size = planet_size
        self.shapesize(*planet_size)
        self.up()
        self.angle = 0
        self.increase_angle = increase_angle
        self.name = name

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.name.xcor() + self.x, self.name.ycor() + self.y)
        self.angle += self.increase_angle


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950

window = Screen()
window.bgcolor('black')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

sun = Turtle()
sun.shape('circle')
sun.shapesize(5, 5)
sun.color('yellow')

earth = Planet(300, 'blue', (1, 1), 0.01, sun)
mercury = Planet(110, 'grey', (0.6, 0.6), 0.05, sun)
venus = Planet(180, 'orange', (0.8, 0.8), 0.03, sun)
mars = Planet(500, 'red', (0.9, 0.9), 0.007, sun)
saturn = Planet(550, 'pink', (0.8, 0.8), 0.008, sun)

moon = Planet(40, 'grey', (0.2, 0.2), 0.06, earth)
phobos = Planet(40, 'grey', (0.2, 0.2), 0.06, mars)
deimos = Planet(35, 'white', (0.2, 0.2), 0.08, mars)

planets = [earth, mercury, venus, mars, moon, phobos, deimos, saturn]

asteroid_list = []
asteroid_list_saturn = []
angle = 0.001

for i in range(200):
    asteroid = Planet(random.randint(610, 750), 'grey', (0.2, 0.2), 0.01, sun)
    asteroid_list.append(asteroid)
    asteroid.increase_angle += angle
    angle += 0.012421

for i in range(100):
    saturn_asteroid = Planet(random.randint(25, 30), 'grey', (0.1, 0.1), 0.01, saturn)
    asteroid_list_saturn.append(saturn_asteroid)
    saturn_asteroid.increase_angle += angle
    angle += 0.001242

window.listen()

while True:
    window.update()
    for planet in planets:
        planet.move()

    for asteroid in asteroid_list:
        asteroid.move()
        asteroid.angle += 0.002

    for saturn_asteroid in asteroid_list_saturn:
        saturn_asteroid.move()
        saturn_asteroid.angle += 0.0001

    time.sleep(0.02)
