class Car:

    def __init__(self, name: str, make: int, model: str, order=None):
        self.name = name
        self.make = make
        self.model = model
        self.__code = '234' #private
        self._idx = '12' #protected

    def start(self):
        print(f'Your new car created, its name: {self.name}')

    def get_code(self):
        return self.__code #getter

    def set_code(self, year: int):
        self.__code = year # setter


mercedes = Car('Mercedes', 2022, 'X6')
mercedes.start()
honda = Car('Honda', 1998, 'A1')
honda.start()
print(honda.make)
print(dir(mercedes))
print(mercedes._Car__code)
print(mercedes.get_code())
mercedes.set_code(200)
print(mercedes.get_code())