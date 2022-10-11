from random import randrange
from tabulate import tabulate


def throw_two_dice(dice_max: int) -> int:
    """Emulate dice throw"""
    dice1 = randrange(1, dice_max + 1)
    dice2 = randrange(1, dice_max + 1)
    return dice1 + dice2


def run_throw_dice_stats(run_limit: int, dice_max: int) -> dict[int, int]:
    """Count current dice stats"""
    current_result = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                      7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for i in range(run_limit):
        throw = throw_two_dice(dice_max)
        current_result[throw] += 1
    return current_result


def calc_dice_statistics(current_result: dict[int, int], run_limit: int):
    """Calc expected and real dice statistics"""
    expected_result = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
                       7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
    result_stat = []
    for count, result in current_result.items():
        line = count, result / run_limit * 100, expected_result[count]
        result_stat.append(line)
    return result_stat


def print_result_statistics(result_stat: list[tuple[int, float, float]]) -> None:
    """Print result table dice statistics"""
    headers = ('Dice number', 'Real', 'Expected')
    result_table = tabulate(result_stat, headers)
    print(result_table)


def main(run_limit: int, dice_max: int) -> None:
    """Main controller"""
    current_result = run_throw_dice_stats(run_limit, dice_max)
    result_stat = calc_dice_statistics(current_result, run_limit)
    print_result_statistics(result_stat)


if __name__ == '__main__':
    RUN_LIMIT = 1000
    DICE_MAX = 6
    main(RUN_LIMIT, DICE_MAX)
