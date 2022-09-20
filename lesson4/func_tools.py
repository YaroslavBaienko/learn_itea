def calc_words_len(data: list[str]) -> list:
    return list(map(str.upper, data))


names = ['Misha', 'Grisha', 'Shisha']
print(calc_words_len(names))

numbers = [2, 3, 4]

squares = list(map(lambda x: x * 2, numbers))
print(squares)

scores = [23, 34, 2342, 234, 34, 98]


def is_A_student(score):
    return score > 75


over_75 = list(filter(is_A_student, scores))
print(over_75)

numbers = [44, 23, 134, 54]


def custom(first, second):
    return first + second
