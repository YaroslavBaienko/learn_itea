class Person:
    def __init__(self, full_name):
        self.full_name = full_name

    def __str__(self):
        return f'{self.__class__}: {self.full_name}'

    def __len__(self):
        return len(self.full_name)


class Point:
    def __init__(self, *args):
        self.__coordinates = args
        print(self.__coordinates)

    def __len__(self):
        return len(self.__coordinates)

    def __abs__(self):
        return tuple(map(abs, self.__coordinates))


if __name__ == '__main__':
    john = Person('John Doe')
    print(john)
    print(len(john))
    point = Point(-1, 2, 3)
    print(len(point))
    print(abs(point))
    Person('Иванов Иван Иванович', 36, 'ВР-415141', 101.3)
