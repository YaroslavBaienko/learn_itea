"""Find chemical elements"""
import re
from prettytable import PrettyTable
from typing import NamedTuple


class Element(NamedTuple):
    """Type class for element"""
    num: str
    abbr: str
    name: str


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def check_element_format(element: str):
    """Check element format like '1,H,Hydrogen'"""
    match = re.match(r'[0-9]+,([A-Z]|[A-Z][a-z]+),[A-Z][a-z]+', element)
    if match:
        return True
    return False


def read_elements_from_file(filename: str):
    """Read data from txt file"""
    elements = []
    with open(filename) as elements_file:
        for element in elements_file:
            element = element.strip()
            if check_element_format(element):
                num, abbr, name = element.split(',')
                element = Element(num, abbr, name)
                elements.append(element)
    return elements


def find_element(elements: list[Element], user_search: str):
    """Find element"""
    result_element = [element for element in elements if user_search.capitalize() in element]
    return result_element.pop() if result_element else False


def print_result_table(element: Element):
    """Print chemical element"""
    element_table = PrettyTable()
    element_table.field_names = ['№', 'Abbr', 'Name']
    element_table.add_row([element.num, element.abbr, element.name])
    print(element_table)


def main(filename: str, user_search):
    """Main controller"""
    check = check_type_exist(filename)
    if check:
        print(check)
        exit()
    elements = read_elements_from_file(filename)

    find_result = find_element(elements, user_search)
    if find_result:
        print_result_table(find_result)
        exit()
    print(f'Element {user_search} not found')


if __name__ == '__main__':
    file = 'elements.txt'
    user_search = 'Hydrogen'
    main(file, user_search)
