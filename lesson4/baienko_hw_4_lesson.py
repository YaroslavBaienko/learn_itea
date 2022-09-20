# Написати функцію, яка сортує список, але всі парні числа мають залишитись на своєму місці.
#
# Приклади:
#
# sort_array([3, 1]) -> [1, 3]
# sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
# sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]
def sort_array(numbers: list) -> list:
    odds = sorted([odd for odd in numbers if odd % 2 != 0], reverse=True)
    result = []
    for odd in numbers:
        if odd % 2 == 0:
            result.append(odd)
        else:
            result.append(odds.pop())
    return result


if __name__ == '__main__':
    CASES = (
        ([3, 1], [1, 3]),
        ([3, 2, -1, 4], [-1, 2, 3, 4]),
        ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4])
    )
    for case, answer in CASES:
        assert sort_array(case) == answer
