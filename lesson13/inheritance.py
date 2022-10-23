class Vehicle:
    def vehicle_method(self):
        print('This is method of class Vehicle')


class Car(Vehicle):
    def car_method(self):
        print('This is method of class Car')


car = Car()
car.vehicle_method()
car.car_method()
