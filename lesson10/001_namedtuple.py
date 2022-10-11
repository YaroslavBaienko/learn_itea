from collections import namedtuple

Car = namedtuple('Car', 'model color mileage')

cars = [
    Car('Lexus', 'red', 10000),
    Car('Mazda', 'green', 12000),
    Car('BMW', 'red', 5000),
    Car('Mitsubishi', 'red', 4000),
    Car('Citroen', 'red', 500),
]

for car in cars:
    print(f'Model: {car.model}')
    print(f'Color: {car.color}')
    print(f'Mileage: {car.mileage}')
    print("*" * 25)

cars_order_color = sorted(cars, key=lambda car: car.mileage, reverse=True)
print(cars_order_color)
