import re

from config import *





class Validator:
    MIN_AGE = MIN_AGE
    MAX_AGE = MIN_AGE

    MIN_WEIGHT = MIN_WEIGHT
    MAX_WEIGHT = MIN_WEIGHT
    def __init__(self, full_name: str, age: int, id_number: str, weight: float):
        self.__full_name = full_name
        self.__age = age
        self.__id_number = id_number
        self.__weight = weight

    @staticmethod
    def check_full_name(arg):
        return re.findall('[А-яА-я]{2,25}\s[А-яА-я]{2,25}\s[А-яА-я]{2,25}', arg) and \
               len(arg.split()) == 3 and \
               arg.split()[0][0] == arg.split()[0][0].upper() and \
               arg.split()[1][0] == arg.split()[1][0].upper() and \
               arg.split()[2][0] == arg.split()[2][0].upper()


    @staticmethod
    def check_id_number(arg):
        return arg.split("-")[0].isalpha() and \
               arg.split("-")[1].isdigit() and \
               len(arg.split("-")[1]) == 6


    @staticmethod
    def check_age(arg):
        return MIN_AGE <= arg <= MAX_AGE and \
               isinstance(arg, int)


    @staticmethod
    def check_weight(arg):
        return MIN_WEIGHT <= arg <= MAX_WEIGHT and \
               isinstance(arg, float)