persons = ['bob', 'fred', 'mike']
special_letters = 'bcf'
persons_report = []

for person in persons:  # O(n)
    for letter in persons:  # O(n ** 2)
        if letter in special_letters:  # O(n ** 3)
            persons_report.insert(0, person)  # O(n ** 4)


user_number = int(input('Enter a number: '))

for i in range(2 ** 32):
    print(i)

