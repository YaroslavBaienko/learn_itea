from string import ascii_letters
from typing import NamedTuple
import re


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class Person:
    def __init__(self, obj: PersonData):
        self.__check = PersonVerify
        self.__check.verify_all(obj)

        self.__full_name = obj.full_name
        self.__age = obj.age
        self.__id_card = obj.id_card
        self.__weight = obj.weight

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__check.verify_full_name(full_name)
        self.__full_name = full_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__check.verify_age(age)
        self.__age = age

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, id_card: str):
        self.__check.verify_id_card(id_card)
        self.__id_card = id_card

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__check.verify_weight(weight)
        self.__weight = weight

    def __str__(self):
        return self.__full_name


class PersonVerify:
    RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    LETTERS = ascii_letters + RUS + RUS.upper()
    AGE_RANGE = range(16, 66)
    WEIGHT_RANGE = range(50, 120)
    CARD_FORMAT = re.compile(r'\w{2}-\d{6}')

    @classmethod
    def verify_all(cls, data: PersonData):
        cls.verify_full_name(data.full_name)
        cls.verify_age(data.age)
        cls.verify_weight(data.weight)
        cls.verify_id_card(data.id_card)

    @classmethod
    def verify_full_name(cls, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError('Full name must be a string')

        full_name = full_name.split(' ')

        if not [value for value in full_name if value]:
            raise TypeError('Full name must contain at least one character')

        if len(full_name) != 3:
            raise TypeError('Invalid name format')

        for name in full_name:
            if len(name.strip(cls.LETTERS)) != 0:
                raise TypeError('Full name can only contain letter')

    @classmethod
    def verify_age(cls, age: int):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age not in cls.AGE_RANGE:
            raise ValueError(f'Age must be between {cls.AGE_RANGE[0]} and {cls.AGE_RANGE[-1]}')

    @classmethod
    def verify_weight(cls, weight: float):
        if not isinstance(weight, float):
            raise TypeError('Weight must be an float number')

        if round(weight) not in cls.WEIGHT_RANGE:
            raise ValueError(f'Weight should be between {cls.WEIGHT_RANGE[0]} and {cls.WEIGHT_RANGE[-1]}')

    @classmethod
    def verify_id_card(cls, id_card: str):
        if not isinstance(id_card, str):
            raise TypeError('Invalid data type for card id')

        if cls.CARD_FORMAT.match(id_card) is None:
            raise ValueError('Invalid card id data format XX-XXXXXX')


if __name__ == '__main__':
    person_data = PersonData('Иванов Иван Иванович', 36, 'ВР-415141', 101.3)
    person = Person(person_data)
    print(person.full_name)
    person.full_name = 'Петров Петр Петрович'
    print(person.full_name)
