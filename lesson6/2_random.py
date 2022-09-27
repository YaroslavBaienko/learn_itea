from random import (
    random,
    randint,
    randrange,
    shuffle,
    choice)

# number_float = random()
# number_int = round(random() * 100)
# print(number_int)

# stop = 100
# random_numbers = [round(random() * 100) for _ in range(stop)]
#
# print(len(random_numbers))
# print(random_numbers)

# random_int = randint(1, 2 ** 32)
# print(random_int)


# randon_range = randrange(1, 100, 2)
# print(list(range(1, 100, 2)))
# print(randon_range)

names = ['bob', 'fred', 'rob']
random_choice_name = choice(names)

random_numbers = [round(random() * 100) for _ in range(100)]
random_choice_number = choice(random_numbers)

print(random_choice_number)
print(random_choice_name)

print(names)
shuffle(names)
print(names)
