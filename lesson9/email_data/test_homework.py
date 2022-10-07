"""Show most usable domain from emails messages"""
import re
import os
from functools import lru_cache
from prettytable import PrettyTable
from collections import Counter
from datetime import datetime


def calc(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func_data = func(*args, **kwargs)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        return func_data
    return wrapper


def check_file(data: str) -> bool:
    """Check is file exist and right file format"""
    try:
        open(data).readline()
    except FileNotFoundError:
        print(f"Файл {data} не найден")
        return True
    except UnicodeDecodeError:
        print(f"Файл {data} не может быть прочитан")
        return True


def read_file(data: str) -> str:
    """Read file in str text"""
    with open(data) as txt_file:
        words = txt_file.read().split()
        text = ' '.join(words)
    return text


def find_emails(data: str) -> list:
    """Parse txt file and find emails using regular expression"""
    emails = re.findall(r'(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', data)
    emails_domain = [i[1:] for i in emails]
    return emails_domain


def make_email_domain_stats(data: list) -> list:
    """Sort most usable domains"""
    stats = Counter(data)
    stats_sorted = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    return stats_sorted


def print_stats_table(data: list) -> classmethod:
    """Printing table with domain usage statistic"""
    table = PrettyTable()
    table.field_names = ('Position', 'Domain', 'Emails quantity')
    for pos in range(len(data)):
        domain = data[pos][0]
        qty = data[pos][1]
        table.add_row([pos+1, domain, qty])
    return table


@calc
def main(data: str):
    check = check_file(filename)
    if check:
        exit()
    file = os.path.join(data)
    text = read_file(file)
    emails = find_emails(text)
    stats_sorted = make_email_domain_stats(emails)
    table = print_stats_table(stats_sorted)
    print(table)


if __name__ == '__main__':
    filename = 'mbox.txt'
    main(filename)
