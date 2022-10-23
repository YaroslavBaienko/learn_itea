class Car:
    def __init__(self):
        print('Start engine')
        self.name = 'corolla'
        self.__make = 1999
        self._model = 'toyota'

    def get_make(self):
        return self.__make

    def set_make(self, year):
        self.__make = year


car = Car()
# print(car.name)
# print(car._model)
# print(dir(car))
# print(car._Car__make)
print(car.get_make())
car.set_make(2010)
print(car.get_make())
