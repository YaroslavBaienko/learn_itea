class Car:
    car_count = 0


    @staticmethod
    def get_class_details():
        print('This is a class "Car"')

    def __str__(self):
        return f'Instance of Car: {self.name}'

    def start(self, name, make, model):
        print('Start engine')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
        print(f"""
        'Start engine' 
        name: {self.name}
        """)


mercedes = Car()
mercedes.start('Mercedes', 2008, 'A1')
bmw = Car()
bmw.start('BMW', 2008, 'X3')

print(Car.car_count)
print(bmw.model)
Car.get_class_details()