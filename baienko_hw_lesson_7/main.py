"""Напишите программу, которая будет считывать файл, содержащий информацию о химических элементах, и сохранять ее в
более подходящей для этого структуре данных. После этого пользователь должен ввести значение. Если введенное значение
окажется целочисленным, программа должна вывести на экран обозначение и название химического элемента с введенным
количеством протонов. При вводе пользователем строки необходимо отобразить количество протонов элемента с введенным
пользователем обозначением или названием. Если введенное пользователем значение не соответствует ни одному из
элементов в файле, необходимо вывести соответствующее сообщение об ошибке. Позвольте пользователю вводить значения до
тех пор, пока он не оставит ввод пустым. """


def read_work_info_from_text_file(filename: str):
    """Read info from text files"""
    work_info = list()
    with open(filename, "rt", encoding="utf-8-sig") as text_file:
        for line in text_file:
            work_info.append(line.split())
    return work_info


def get_name_and_symbol_by_protons(protons: str, work_info: list):
    for item in work_info:
        if item[0].split(',')[0] == protons:
            return item[0].split(',')[1], item[0].split(',')[2]
    return 'There are no element with such parameters. Try again!'


def get_protons_and_symbol_by_name(name: str, work_info: list):
    for item in work_info:
        if item[0].split(',')[2] == name:
            return item[0].split(',')[0], item[0].split(',')[1]
    return 'There are no element with such parameters. Try again!'


def get_protons_and_name_by_symbol(symbol: str, work_info: list):
    for item in work_info:
        if item[0].split(',')[1] == symbol:
            return item[0].split(',')[0], item[0].split(',')[2]
    return 'There are no element with such parameters. Try again!'


def main(attribute: str):
    if attribute.isdigit():
        result = get_name_and_symbol_by_protons(attribute, read_work_info_from_text_file('elements.txt'))
    elif 1 <= len(attribute) <= 3:
        result = get_protons_and_name_by_symbol(attribute, read_work_info_from_text_file('elements.txt'))
    else:
        result = get_protons_and_symbol_by_name(attribute, read_work_info_from_text_file('elements.txt'))
    return result


if __name__ == '__main__':
    while True:
        attribute = input('Enter information to find or tap "Enter" to quit: ')
        if attribute == '':
            break
        else:
            print(main(attribute=attribute))
