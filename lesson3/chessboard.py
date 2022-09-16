import string


def make_chessboard(size=8):
    """Make chessboard structure data"""
    if size >= len(string.ascii_lowercase):
        raise ValueError(f"Max size must be less the {len(string.ascii_lowercase)}")
    letters = string.ascii_lowercase[:size]
    chessboard = {}
    color = 0
    counter = 0

    for letter in letters:
        for number in range(1, size + 1):
            cell = letter + str(number)
            if counter % 2 == 0:
                color = 1
            else:
                color = 0
            chessboard[cell] = color
            counter += 1
        if color:
            counter = 0
        else:
            counter = 1

    return chessboard


def check_data_type(data):
    return isinstance(data, str)


def check_cell(data, cell):
    return cell in data


def find_cell_color(data, cell):
    if data[cell]:
        return 'black'
    return 'white'


def main(cell='a1'):
    chessboard = make_chessboard()

    flag_type = check_data_type(cell)
    if not flag_type:
        raise TypeError(f'Invalid data type: {type(cell)}')

    flag_value = check_cell(chessboard, cell)
    if not flag_value:
        raise ValueError(f'Cell not found in chessboad {cell}')

    cell_color = find_cell_color(chessboard, cell)
    return cell_color


if __name__ == '__main__':
    cell = 'a101'

    try:
        print(main(cell=cell))
    except ValueError:
        print('Value error')
