print(int(True))
first_name = 'bob'
last_name = 'smith'
menu = """
one
two
three
"""
print(first_name, last_name)
print(menu)

sentence = "Welcome, \"John Smith\""

sentence2 = r"Welcome,\n\r'John'"
print(sentence2)

print(id(first_name))

full_name = first_name.capitalize() + " " + last_name.capitalize()
print(full_name)

full_name = f'{first_name.capitalize()} {last_name.capitalize()}'
print(full_name)
from string import ascii_lowercase, ascii_letters, punctuation


def find_letters_qty(data):
    data = data.lower()
    letters_count = {}
    for char in data:
        if char.lower() in ascii_letters:
            letters_count[char.lower()] = 0

    for letter in letters_count:
        letters_count[letter.lower()] = data.count(letter)

    return letters_count


full_name = 'John Doe! 777'

print(find_letters_qty(full_name))

full_name = full_name[::-1]
print(full_name)
