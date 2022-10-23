class Car:

    def __init__(self, name: str, make: int, model: str):
        self.name = name
        self.make = make
        self.model = model

    def start(self):
        print(f'{self.name} start engine')


mercedes = Car('mercedes', 2008, 'c200')
mercedes.start()

honda = Car('honda', 2010, 'civic')
honda.start()

print(id(mercedes), id(honda))

# print(dir(mercedes))
# print(mercedes.name)
#
# print(honda.name)
#
# print(Car.car_count)

