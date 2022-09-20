def find_average_square_diff(numbers1, numbers2):
    join_numbers = zip(numbers1, numbers2)
    abs_diff = []
    for first, second in join_numbers:
        # if first >= second:
        #     diff = first - second
        # else:
        #     diff = second - first
        diff = second - first if first >= second else first - second
        abs_diff.append(diff ** 2)
    return sum(abs_diff) / len(numbers1)


if __name__ == '__main__':
    # [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
    # print(find_average_square_diff([1, 2, 3], [4, 5, 6]))

    CASES = (
        ([1, 2, 3], [4, 5, 6], 9)
    )

    for list_a, list_b, answer in CASES:
        print(find_average_square_diff(list_a, list_b))