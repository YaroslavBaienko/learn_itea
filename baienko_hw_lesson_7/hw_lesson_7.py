"""Напишите программу, которая будет считывать файл, содержащий информацию о химических элементах, и сохранять ее в
более подходящей для этого структуре данных. После этого пользователь должен ввести значение. Если введенное значение
окажется целочисленным, программа должна вывести на экран обозначение и название химического элемента с введенным
количеством протонов. При вводе пользователем строки необходимо отобразить количество протонов элемента с введенным
пользователем обозначением или названием. Если введенное пользователем значение не соответствует ни одному из
элементов в файле, необходимо вывести соответствующее сообщение об ошибке. Позвольте пользователю вводить значения до
тех пор, пока он не оставит ввод пустым. """
import os


def read_and_convert_textfile_to_normal_data(filename: str) -> [dict]:
    """Read info from text files and convert it to the elements dictionary"""
    with open(filename, "rt", encoding="utf-8-sig") as text_file:
        work_info = [elements.strip() for elements in text_file.readlines()]
        work_info = [items.split(',') for items in work_info]
        normalized_data = [{'protons': values[0], 'symbol': values[1], 'element': values[2]} for values in work_info]
    return normalized_data


def get_elements_data(parameter: str, elements_block: [dict]) -> str:
    """Get all elements as a dictionary by just one of the element parameters"""
    if parameter.isdigit():
        for dic in elements_block:
            if parameter == dic['protons']:
                return dic
            else:
                continue
    if len(parameter) >= 1 or len(parameter) <= 3:
        for dic in elements_block:
            if parameter == dic['symbol']:
                return dic
            else:
                continue
    if len(item) > 3:
        for dic in elements_block:
            if parameter == dic['element']:
                return dic
            else:
                continue
    return 'There are no element with such parameter. Try again!'


if __name__ == '__main__':
    current_dir = os.getcwd()
    current_read_file = os.path.join(current_dir, 'elements.txt')
    data = read_and_convert_textfile_to_normal_data(current_read_file)
    while True:
        item = input('Enter the parameter of element you want to get or tap "Enter" to quit: ')
        if item == '':
            quit()
        else:
            print(get_elements_data(item, data))
