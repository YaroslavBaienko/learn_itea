# A = 23
# print(id(A))
# B = A
# print(id(B))
# A = 0
# print(id(B))
# print(id(A))
# persons = ['John', 'Jane', 'Bob']
# print('Persons', id(persons))
# temp_persons = persons
# temp_persons.append('new')
# print(persons, temp_persons)
#
# number = 16
# str_number = str(number)
# print(str_number)
#
# name = 'bob'
# print(name.capitalize())
#
# print(dir(__builtins__))
# # нажимаем Ctrl и наводим на метод, чтоб увидеть его реализацию, то же и для функций
# number = int(input('Please, enter number '))
# print(type(number))
#
# numbers = [1, None, [1, 2], 4, 5]
# print(numbers[0])
# id = 100
#
# # 0 - notation
# # o(1)
# number = 1
# number += 1
# str_number = str(number)
# print(str_number)
#
# qty = input('Enter a qty: ')
# numbers = [number for number in range(qty)]
# print(numbers)
#
# words = input('Enter words: ').split('')
#
# for word in words:
#     for letter in word:
#         print(letter)
#
# # разные способы поиска
from random import randint, choice


#

def find_number(numbers: list[int], value: int) -> int:
    """
    Find number in list of numbers
    :param numbers:
    :param value:
    :return:
    """
    for index, number in enumerate(numbers):
        if number == value:
            return index
    return -1


numbers = [randint(1, 100) for _ in range(20)]
print(numbers)

random_number = choice(numbers)
print(random_number)
print('Index of choosen number is: ', find_number(numbers, random_number))
