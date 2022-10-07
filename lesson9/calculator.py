def check_nums(first_num: str, second_num: str):
    """Check numbers of float"""
    try:
        float(first_num)
        float(second_num)
    except TypeError as error:
        return str(error)
    return False

def check_op(operator: str):
    """Check user value in +,-,*,/"""
    return False if operator in {"+", "-", "*", "/"} else True

def get_user_input():
    """Get nums and operator"""
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    operator = input("Enter operator: ")
    return first_num, second_num, operator

def calc_result(first_num: float, second_num: float, operator:str):
    """Calculate numbers"""
    if operator == "/" and not second_num:
        return "Zero division error"
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda  a, b: a / b
    }
    return operations[operator](first_num, second_num)

def main():
    """Main controller"""
    first_num, second_num, operator = get_user_input()
    check_numbers = check_nums(first_num, second_num)
    check_operator = check_op(operator=operator)
    if any((check_numbers, check_operator)):
        print("Value error")
        exit()
    first_num, second_num = float(first_num), float(second_num)
    result = calc_result(first_num, second_num, operator)
    print(result)


if __name__ == '__main__':
    main()