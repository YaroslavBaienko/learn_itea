def pow_digit(number):
    return sum(int(digit) ** pow for pow, digit in enumerate(str(number), 1))


def sum_digit_pow(start, limit):
    return [number for number in range(start, limit + 1) if number == pow_digit(number)]


# def pow_digit(number):
#     pow_digits = []
#     for pow, digit in enumerate(str(number), 1):
#         temp = int(digit) ** pow
#         pow_digits.append(temp)
#     return sum(pow_digits)
#
#
# def sum_digit_pow(start, limit):
#     special_numbers = []
#     for number in range(start, limit + 1):
#         if number == pow_digit(number):
#             special_numbers.append(number)
#     return special_numbers




print(sum_digit_pow(1, 135) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135])
