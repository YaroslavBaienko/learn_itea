from random import random, randint, randrange

count = 0
source = list()
while count < 10000000:
    source.append(randint(2, 100000000000))
    count += 1

for number in source:
    if number < 2000000:
        print(hex(number))



