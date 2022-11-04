import random

from cross_game.game_lib.sprites.car import Car
from cross_game.settings.game_settings import COLORS


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.pause = False

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-245, 245)
            new_car.goto(310, random_y)

            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if not self.pause:
                car.move()

            if car.xcor() < -400:
                car.hideturtle()

    @staticmethod
    def increase_speed():
        Car.move_increment += 1
