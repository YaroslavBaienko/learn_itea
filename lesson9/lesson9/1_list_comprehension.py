import math

names = ['bob', 'mike', 'rich']
accepted_names = ['bob', 'rich']

names_upper = []

for name in names:
    if name in accepted_names:
        names_upper.append(name.upper())

print(names)
print(names_upper)

names_upper = [name.title() for name in names if name in accepted_names]
print(names_upper)

squares_for = []

for x in range(10):
    if x % 2 == 0:
        squares_for.append(x ** 2)

squares = [math.atan2(x ** 2, 2) for x in range(10) if x % 2 == 0]
print(squares)
print(squares_for)

print('bob tom'.title())
print('bob tom'.capitalize())

last_name = names.pop()
print(last_name)

# def some_func():
#     global names
#
