# Число 89 є першим цілим числом з більш ніж однією цифрою, яке відповідає властивості
# Тому що ця сума дає те саме число.
# Фактично: 89 = 8^1 + 9^2
#
# Наступним числом, що володіє цією властивістю, є 135.
#
# Перегляньте цю властивість ще раз: 135 = 1^1 + 3^2 + 5^3
#
# Нам потрібна функція для збору цих чисел, яка може отримати два цілих числа a, b, які визначають діапазон [a,
# b] (включно) і виводять список відсортованих чисел у діапазоні, що відповідає властивості, описаній вище.
#
# Розгляньмо деякі випадки (введення -> вихід):
#
# 1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# Якщо в діапазоні [a, b] таких чисел немає, функція має вивести порожній список.
#
# 90, 100 --> []


def is_valid(number):
    return sum(int(digit) ** idx for idx, digit in enumerate(str(number), 1))


def sum_with_power(first: int, last: int) -> list:
    """
    Function takes a number and sum its digits
    raised to the corresponding powers
    :param first: int
    :param last: int
    :return: list
    """
    return [number for number in range(first, last + 1) if number == is_valid(number)]


if __name__ == '__main__':
    CASES = (
        ((1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ((1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]),
        ((90, 100), [])
    )
    for case, answer in CASES:
        assert sum_with_power(*case) == answer
