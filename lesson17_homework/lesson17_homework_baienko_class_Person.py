import re


class Person:
    MIN_AGE = 16
    MAX_AGE = 66

    MIN_WEIGHT = 40
    MAX_WEIGHT = 130

    def __init__(self, full_name: str, age: int, id_number: str, weight: float):
        self.__full_name = full_name
        self.__age = age
        self.__id_number = id_number
        self.__weight = weight

        if self.__check_full_name(full_name):
            self.__full_name = full_name
        else:
            raise ValueError(
                'First argument need to be only cyrillic, contain 3 words '
                'without spaces, all words with first uppercase letter'
            )

        if self.__check_age(age):
            self.__age = age
        else:
            raise ValueError('Second argument must be only integer from 16 to 66')

        if self.__check_id_number(id_number):
            self.__id_number = id_number
        else:
            raise ValueError(
                '3rd argument must be in the next format for example "АВ-344576"'
            )

        if self.__check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError(
                '4th argument can be only float with amount from 40.0 to 130.0"'
            )

    @staticmethod
    def __check_full_name(arg):
        return re.findall('[А-яА-я]{2,25}\s[А-яА-я]{2,25}\s[А-яА-я]{2,25}', arg) and \
               len(arg.split()) == 3 and \
               arg.split()[0][0] == arg.split()[0][0].upper() and \
               arg.split()[1][0] == arg.split()[1][0].upper() and \
               arg.split()[2][0] == arg.split()[2][0].upper()

    @staticmethod
    def __check_id_number(arg):
        return arg.split("-")[0].isalpha() and \
               arg.split("-")[1].isdigit() and \
               len(arg.split("-")[1]) == 6

    @classmethod
    def __check_age(cls, age):
        return cls.MIN_AGE <= age <= cls.MAX_AGE and \
               isinstance(age, int)

    @classmethod
    def __check_weight(cls, weight):
        return cls.MIN_WEIGHT <= weight <= cls.MAX_WEIGHT and \
               isinstance(weight, float)

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if self.__check_full_name(full_name):
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
        if self.__check_age(age):
            self.__age = age
        else:
            raise ValueError('Second argument must be only integer from 16 to 66')

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if self.__check_id_number(id_number):
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
        if self.__check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError(
                '4th argument can be only float"'
            )


yaroslav = Person("Баенко Ярослав Владимирович", 33, "КМ-874744", 69.0)

print(Person._Person__check_full_name("Ярослав Владимирович Баенко"))
yaroslav.full_name = "Петров Владимир Степанович"

print(yaroslav.full_name)
yaroslav.weight = 89.0
yaroslav.age = 23
