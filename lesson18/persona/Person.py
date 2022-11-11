import re
from Validator import *

class Person:
    MIN_AGE = MIN_AGE
    MAX_AGE = MIN_AGE

    MIN_WEIGHT = MIN_WEIGHT
    MAX_WEIGHT = MIN_WEIGHT

    def __init__(self, full_name: str, age: int, id_number: str, weight: float):
        self.__full_name = full_name
        self.__age = age
        self.__id_number = id_number
        self.__weight = weight


        if Validator.check_full_name(full_name):
            self.__full_name = full_name
        else:
            raise ValueError(
                'First argument need to be only cyrillic, contain 3 words '
                'without spaces, all words with first uppercase letter'
            )

        if Validator.check_age(age):
            self.__age = age
        else:
            raise ValueError('Second argument must be only integer from 16 to 66')

        if Validator.check_id_number(id_number):
            self.__id_number = id_number
        else:
            raise ValueError(
                '3rd argument must be in the next format for example "АВ-344576"'
            )

        if Validator.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError(
                '4th argument can be only float with amount from 40.0 to 130.0"'
            )



    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if Validator.check_full_name(full_name):
            self.__full_name = full_name
        else:
            raise ValueError(
                'First argument need to be only cyrillic, contain 3 words '
                'without spaces, all words with first uppercase letter'
            )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if Validator.check_age(age):
            self.__age = age
        else:
            raise ValueError('Second argument must be only integer from 16 to 66')

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if Validator.check_id_number(id_number):
            self.__id_number = id_number
        else:
            raise ValueError(
                '3rd argument must be in the next format for example "АВ-344576"'
            )

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if Validator.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError(
                '4th argument can be only float"'
            )


yaroslav = Person("Баенко Ярослав Владимирович", 33, "КМ-874744", 69.0)


yaroslav.full_name = "Петров Владимир Степанович"

print(yaroslav.full_name)
yaroslav.weight = 89.0
yaroslav.age = 23
yaroslav.age = 45
print(yaroslav.age)
