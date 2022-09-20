# def multiply_all(numbers):
#     return lambda power: [number * power for number in numbers]
#
#
# print(multiply_all([1, 2, 3])(2))

# names = ['bob', 'james', 'brown']
#
# names_upper = []
# for name in names:
#     names_upper.append(name.title())
#
# names = [name.title() for name in names]
# print(names)

limit = 10

for j in range(1, limit + 1):
    print(f'{j}: ', end='')
    for k in range(1, limit + 1):
        print(f'{k}', end=' ')
    print()

print(len('abc'))

persons = {
    'John Doe': {
        'age': 25,
        'position': 'python web dev'
    }
}

for person, values in persons.items():
    print(f'Person "{person}" ', end='')
    for key, value in values.items():
        print(f'{key} : {value}', end=' ')
    print()


numbers = [second for number in range(10) for second in range(10)]
print(numbers)
