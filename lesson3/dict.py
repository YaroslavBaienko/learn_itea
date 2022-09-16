person1 = {
    'name': 'Bob',
    'last name': 'Baienko',
    'age': 34
}

person2 = {
    'name': 'Bob',
    'last name': 'Baienko',
    'age': 34
}

person3 = {
    'name': 'Bob',
    'last name': 'Baienko',
    'age': 34
}

persons = [person1, person2, person3]
# print(persons)
#
# for key in persons:
#     print(f'{key}: {persons[key]}')
#
# for key, value in persons.items():
#     print(key, ":", value)
#
# persons['department'] = 'design dept'
#
# print(persons)
#
#
# if 'stage' in persons:
#     print(persons['stage'])
# else:
#     persons['stage'] = 4
#
# print(persons)

for person in persons:
    print('*' * 25)
    for key in person:
        print(f'{key}: {person[key]}')
    print('*' * 25)


persons = []
persons_qty = {}
person = ''

if persons_qty:
    print(persons_qty)
else:
    print('empty')