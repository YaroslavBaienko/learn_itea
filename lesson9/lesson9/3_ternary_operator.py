from random import randint


number = 1
check = print if number % 2 == 0 else len

if number % 10 == 0:
    number = 0

print(check('bob'))

# numbers_rand = [randint(1, 100) if x % 2 == 0 else False
#                 for x in range(10)]
# print(numbers_rand)
