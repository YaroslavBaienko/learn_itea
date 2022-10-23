class Car:
    name = 'c200'
    make = 'mercedes'
    model = 2008
    price = 1000

    def start(self):
        print(f'Start engine {self.name}')

    def stop(self):
        print('Stop engine')

    def __add__(self, other):
        return self.price + other.price

# print(Car)
# print(type(Car))
# print(Car.name)


mercedes1 = Car()
mercedes2 = Car()
print(mercedes1 + mercedes2 + 15000)

# mercedes.start.__call__
# mercedes.start()


# Car.start(mercedes)
# print(mercedes.name)
# print(dir(mercedes))
# print(mercedes.__class__)
# print(mercedes)
# print(id(mercedes))
