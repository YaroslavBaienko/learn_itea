def calc_words_len(data):
    return list(map(str.upper, data))


names = ['one', 'bill', 'james']
print(calc_words_len(names))

numbers = [2, 3, 4]

squares = map(lambda x: x ** 2, numbers)

for square in squares:
    print(square)
