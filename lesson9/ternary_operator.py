from random import randint
number = 1
check = True if number % 2 == 0 else False
print(check)
numbers_rand = [randint(1, 100) if x % 2 == 0 else False for x in range(10)]
print(numbers_rand)