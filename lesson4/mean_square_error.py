# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
def find_average_square_diff(numbers1, numbers2):
    join_numbers = zip(numbers1, numbers2)
    abs_diff = []
    for first, second in join_numbers:
        diff = second - first if first >= second else first - second
        abs_diff.append(diff ** 2)
    return sum(abs_diff) / len(numbers1)


if __name__ == '__main__':
    CASES = (
        ([1, 2, 3], [4, 5, 6], 9),
        ([10, 20, 10, 2], [10, 25, 5, -2], 16.5),
        ([-1, 0], [0, -1], 1)
    )
    for case in CASES:
        list_a = case[0]
        list_b = case[1]
        answer = case[2]
        assert find_average_square_diff(list_a, list_b) == answer
