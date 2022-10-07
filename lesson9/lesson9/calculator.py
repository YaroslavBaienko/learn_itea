def check_nums(first_num: str, second_num: str):
    """Check numbers of float type"""
    try:
        float(first_num)
        float(second_num)
    except ValueError as error:
        return str(error)
    return False


def check_op(operation: str):
    """Check user value in +,-,*, /"""
    return False if operation in {'+', '-', '*', '/'} else True


def get_user_input():
    """Get nums and operation"""
    first_num = input("Enter first num: ")
    second_num = input("Enter second num: ")
    operation = input("Enter action: ")
    return first_num, second_num, operation


def calculate(first_num: float, second_num: float, operation: str):
    """Calculate numbers"""
    if operation == '/' and not second_num:
        return 'Zero division error'
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    return operations[operation](first_num, second_num)


def main():
    """Main controller"""
    first_num, second_num, operation = get_user_input()
    check_numbers = check_nums(first_num, second_num)
    check_operation = check_op(operation)
    if any((check_numbers, check_operation)):
        print('Value error')
        exit()
    first_num, second_num = float(first_num), float(second_num)
    calc_result = calculate(first_num, second_num, operation)
    print(calc_result)


if __name__ == '__main__':
    main()
