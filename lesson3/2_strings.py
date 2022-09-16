from string import ascii_lowercase


def find_letters_qty(data):
    data = data.lower()
    letters_count = {}

    for char in data:
        if char in ascii_lowercase:
            letters_count[char] = 0

    for letter in letters_count:
        letters_count[letter] = data.count(letter)

    return letters_count


full_name = 'John Doe! 777'

print(find_letters_qty(full_name))

