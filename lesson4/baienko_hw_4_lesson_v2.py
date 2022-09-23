import lesson5.decorators


def sort_array(numbers: list) -> list:
    odds = sorted([odd for odd in numbers if odd % 2 != 0], reverse=True)
    result = []
    [result.append(odd) if odd % 2 == 0 else result.append(odds.pop()) for odd in numbers]
    return result


if __name__ == '__main__':

    CASES = (
        ([3, 1], [1, 3]),
        ([3, 2, -1, 4], [-1, 2, 3, 4]),
        ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4])
    )

    for case, answer in CASES:
        assert sort_array(case) == answer
