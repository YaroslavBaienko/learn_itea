from collections import namedtuple

Car = namedtuple('Car', 'model color mileage')
# Car = namedtuple('Car', ['model', 'color', 'mileage'])


cars = [
    Car('Lexus', 'red', 10000),
    Car('Mazda', 'blue', 12000),
    Car('BMW', 'green', 17600),
]

for car in cars:
    print(f'Model: {car.model}')
    print(f'Color: {car.color}')
    print(f'Mileage: {car.mileage}')
    print('*' * 25)


lists = [
    ('Lexus', 'red', 10000),
    ('Mazda', 'blue', 12000),
    ('BMW', 'green', 17600),
]

for i in lists:
    print(f'Model: {i[0]}')
    print(f'Color: {i[1]}')
    print(f'Mileage: {i[2]}')
    print('*' * 25)


print(
    sorted(
        sum(
            lists
        )
    )
)
