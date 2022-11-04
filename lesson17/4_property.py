class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def age(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    john = Person('John', 25)
    print(john.age)
    john.age = 35
