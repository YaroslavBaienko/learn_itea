"""Program that calculate results of rolling dices and returns statistic table with simulation percent and expected result"""
from random import randint
from collections import Counter
from prettytable import PrettyTable


def roll_dice():
    """Summarize two dice results"""
    first_dice = randint(1, 6)
    second_dice = randint(1, 6)
    return first_dice + second_dice


def create_table(rows: list):
    """Create table using rows"""
    table = PrettyTable()
    table.field_names = ['Result', 'Simulation percent', 'Expected result']
    table.add_rows(rows)
    return table


def main():
    dices = [roll_dice() for _ in range(1000)]
    counter = Counter(dices)
    expected_result = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36,
                       10: 3 / 36,
                       11: 2 / 36, 12: 1 / 36}
    rows = []
    for key in sorted(counter.keys()):
        rows.append([key, round((counter[key] / 1000 * 100), 2), round((expected_result[key] * 100), 2)])
    result_table = create_table(rows)
    return result_table


if __name__ == '__main__':
    print("The variety of 1000 combinations of dices")
    print(main())
