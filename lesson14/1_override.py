class Vehicle:
    def print_details(self):
        print('Class Vehicle')


class Car(Vehicle):
    def print_details(self):
        print('Class Car')


class Cycle(Vehicle):
    def print_details(self):
        print('Class Cycle')


vehicles = [Vehicle() for _ in range(10)]
car = Car()
vehicles.append(car)
vehicles.append(Cycle())


while True:
    for vehicle in vehicles:
        vehicle.print_details()
