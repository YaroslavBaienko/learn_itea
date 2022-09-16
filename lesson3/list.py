persons = ['bob', 'jane', ' rich', 'frank']

for person in persons:
    print(person, len(person))

print(len(persons))

name = 'bob'

for index in range(len(persons)):
    if name == persons[index]:
        persons[index] = name.capitalize()

print(persons[0])
