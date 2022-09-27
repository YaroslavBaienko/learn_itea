"""
В данном упражнении вы должны написать программу, которая будет
находить самое длинное слово в файле. В качестве результата программа
должна выводить на экран длину самого длинного слова и все слова такой
длины. Для простоты принимайте за значимые буквы любые
не пробельные символы, включая цифры и знаки препинания.
"""


def split_text_in_file(file):
    import os
    import re
    current_dir = os.getcwd()
    current_read_file = os.path.join(current_dir, file)
    with open(current_read_file, 'rt') as file:
        file = file.read()
        words_to_check = file.split()
    return words_to_check


def find_longest_word(words: list) -> int:
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length


def print_longest_words(words_to_check: list, length: int) -> str:
    for word in words_to_check:
        if len(word) == length:
            return word


def main():
    file = split_text_in_file('example.txt')
    longest_length = find_longest_word(file)
    to_print = print_longest_words(file, longest_length)
    print(f'The longest word contain {longest_length} symbols. There are words with same length: {to_print}')


if __name__ == "__main__":
    main()
