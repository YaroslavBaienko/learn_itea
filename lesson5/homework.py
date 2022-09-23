from functools import lru_cache


def validate_data_type(data: list[int]) -> bool:
    """
    Data type must be list[int]
    :param:
    :return:
    """
    if not isinstance(data, list):
        return False

    len_numbers = len([number for number in data if isinstance(number, int)])
    return len_numbers == len(data)


def sort_only_odd_numbers(numbers: list[int]) -> list[int] | str:
    """
    Sort only odd numbers
    :param:
    :return:
    """

    odd_sorted = sorted([number for number in iter(numbers) if number % 2 != 0], reverse=True)
    numbers = [odd_sorted.pop() if number % 2 else number for number in numbers]
    return numbers


@lru_cache(maxsize=128)
def main(numbers: list[int]) -> str | None:
    """
    Main controller
    :return:
    """
    if not validate_data_type(numbers):
         return f'Data type must be list[int], not {numbers}'

    result = sort_only_odd_numbers(numbers)
    return result


if __name__ == '__main__':
    assert main([3, 2, -1, 4]) == [-1, 2, 3, 4]

