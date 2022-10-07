import math

names = ['bob', 'mike', 'rich']
accepted_names = ['mike']
names_upper = []
for name in names:
    names_upper.append(name.upper())

print(names)
print(names_upper)

names_upper = [name.title() for name in names if name in accepted_names]
print(names_upper)

squares = [math.atan2(x ** 2, 2) for x in range(10) if x % 2 == 0]
print(squares)


names.insert(1, 'Sergo')
print(names)