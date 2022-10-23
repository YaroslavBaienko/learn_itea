class Car(object):
    car_count = 0

    @staticmethod
    def get_class_name():
        print('This is Car class')

    def __str__(self):
        return self.name

    def start(self, name: str, make: int, model: str):
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
#         print(f"""
# Start engine
# name: {self.name}
#         """)


mercedes = Car()
mercedes.start('mercedes', 2008, 'c200')
print(mercedes.__str__())

# print(mercedes.name)
#
# honda = Car()
# honda.start('honda', 2010, 'civic')
# print(honda.name)
#
# print(Car.car_count)

