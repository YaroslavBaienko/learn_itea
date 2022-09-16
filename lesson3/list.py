persons = ['bob', 'jane', ' rich', 'frank']

for person in persons:
    print(person, len(person))

print(len(persons))

name = 'bob'

for index in range(len(persons)):
    if name == persons[index]:
        persons[index] = name.capitalize()

print(persons[0])
persons.sort(reverse=True)
print(persons)
persons.insert(2, 'black')
print(persons)


# "Задача"
numbers = [5, 10, 15, 20, 25, 20]

searched_value = 20
new_value = searched_value * 10
for index, number in enumerate(numbers):
    if numbers[index] == searched_value:
        numbers[index] = new_value
        break

for _ in range(new_value):
    print(1)


print(numbers)


cousin = {
    'borsch': 200, "look": 300, "salt": 150
}

for index, item in enumerate(cousin):
    print(index, item)