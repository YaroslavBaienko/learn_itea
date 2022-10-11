from collections import namedtuple

Car = namedtuple('Car', 'model color mileage')

cars = [
    Car('Lexus', 'red', 10000),
    Car('Mazda', 'blue', 12000),
    Car('BMW', 'green', 17600),
]

cars_order_color = sorted(cars, key=lambda car: car.mileage, reverse=True)
print(cars_order_color)
