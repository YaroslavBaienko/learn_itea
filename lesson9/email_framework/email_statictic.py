"""Counts how many emails each domain contains and displays a table"""
import os
import re
from pathlib import Path
from datetime import datetime
from functools import lru_cache
from prettytable import PrettyTable
from collections import defaultdict
from tabulate import tabulate

import email_data


def calc_execution_time(func):
    """Calc execution time"""
    def wrapper(*args, **kwargs):
        """Func wrapper"""
        start = datetime.now()
        func_data = func(*args, **kwargs)
        end = datetime.now()
        print(f'Func name {func.__name__}() time: {end - start}')
        return func_data
    return wrapper


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


@lru_cache(maxsize=100)
def get_emails_from_string(line: str):
    """Find emails in string"""
    email_pattern = re.compile(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')
    emails = email_pattern.findall(line)
    if emails:
        email = emails.pop()
        return email
    return False


def get_domains_from_file(path_to_file: str):
    """Get domains from emails log file"""
    domains = defaultdict(int)
    with open(path_to_file) as email_file:
        for line in email_file:
            if line:
                email = get_emails_from_string(line)
                if email:
                    domain = email.split('@').pop()
                    domains[domain] += 1
    return domains


def sort_domains(domains: dict[str: int], order: bool):
    """Sort domains per emails"""
    domains_ordered = {
        domain: qty for domain, qty in sorted(
            domains.items(),
            key=lambda item: item[1],
            reverse=order
        )
    }
    return domains_ordered


def print_email_domain_statistic(emails_in_domains: dict[str: int]):
    """Print how many emails contain domains"""
    result_table = PrettyTable()
    result_table.field_names = ['№', 'Domain', 'Number']
    counter = 1
    for domain, number in emails_in_domains.items():
        result_table.add_row([counter, domain, number])
        counter += 1
    return result_table


@calc_execution_time
def main(path_to_file: str, order: bool = True):
    """Main controller"""
    check = check_type_exist(path_to_file)
    if check:
        print(check)
        exit()
    domains = get_domains_from_file(path_to_file)
    domains = sort_domains(domains, order)
    result_table = print_email_domain_statistic(domains)
    return result_table


def get_path():
    """Get emails path"""
    folder = str(Path(email_data.__file__).parent.absolute())
    file = 'mbox.txt'
    path = os.path.join(folder, file)
    return path


if __name__ == '__main__':
    print(main(get_path()))
