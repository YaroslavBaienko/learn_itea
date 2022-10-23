class Car:
    name = 'C200'
    make = 'mercedes'
    model = 2008
    price = 10000

    def start(self):
        print(f'Заводим двигатель {self.name}')

    def stop(self):
        print('Отключаем двигатель')

    def __add__(self, other):
        return self.price + other.price

my_car = Car()
her_car = Car()
our_cars = my_car + her_car
print(our_cars)
# my_car.start()
# my_car.stop()
#
# my_car.name = 'Godzilla'
# print(my_car.name)
# print(Car)
# print(id(my_car))
# print(type(Car))
my_car.stop()
Car.start(my_car)
my_car.start.__call__
print(dir(my_car))