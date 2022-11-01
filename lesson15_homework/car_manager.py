
from turtle import Turtle
import random

COLORS = ["green", "purple", "yellow", "red", "blue", "orange"]
Y_AXIS = [-250, -210, -170, -130, -90, -50, -40, 0, 40, 80, 120, 160, 200, 240]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if (random.choice([1, 2, 3, 4, 5]) == 5):
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_y = random.choice(Y_AXIS)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
