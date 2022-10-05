"""Count an amount of mails on the same domains ordered by descending"""
import re
from collections import Counter
from tabulate import tabulate


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def read_elements_from_file(filename: str):
    """Read data from txt file"""
    elements = list()
    with open(filename) as elements_file:
        for element in elements_file:
            element = element.strip()
            elements.append(element)
    return elements


def search_all_domains(elements: str):
    """Search all domain names from elements"""
    all_domains = list()
    for element in elements:
        search_result = re.search(r'\@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', element)
        if search_result is not None:
            all_domains.append(search_result.group())
    return all_domains


def main(filename: str):
    """Main controller"""
    check = check_type_exist(filename=filename)
    if check:
        print(check)
        exit()
    elements = read_elements_from_file(filename=filename)
    all_domains = search_all_domains(elements=elements)
    counter = Counter(all_domains)
    result = [(l, k) for k, l in sorted([(j, i) for i, j in counter.items()], reverse=True)]
    return result


if __name__ == '__main__':
    filename = 'mbox.txt'
    result = main(filename=filename)
    print('There are the next amount of mails on the same domains ordered by descending: ')
    table = list()
    sum = 0
    for num in result:
        sum = sum + num[1]
    percentage = list()
    for num in result:
        percent = num[1] * 100 / sum
        percentage.append(percent)
    table = list()
    for domain, nums in result:
        table.append([domain, nums, str((nums * 100) / sum) +' %'])
    print(tabulate(table))

