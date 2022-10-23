from oop import Car

mercedes = Car()
mercedes.start('Mercedes', 2008, 'X6')
print(mercedes)
print(mercedes.__str__())

class Animal:
    animal_count = 0

    def __init__(self):
        Animal.animal_count += 1
        print(Animal.animal_count)

zebra = Animal()
human = Animal()
