import argparse
from argparse import Namespace


def parse_args() -> Namespace:
    """Parse args with argparse"""
    parser = argparse.ArgumentParser(
        prog='Say hello',
        usage='%(prog)s 1_argparse.py --first <firstname> --last <lastname> [--case lower|upper]',
        description='Say hello to any guy'
    )
    parser.add_argument(
        '-f',
        '--first',
        type=str,
        help='enter yor firstname',
        required=True
    )
    parser.add_argument(
        '-l',
        '--last',
        type=str,
        help='enter yor lastname',
        required=True
    )
    parser.add_argument(
        '--case',
        type=str,
        help='enter case of message',
        default='lower',
        required=False
    )
    args = parser.parse_args()
    return args


def say_hello_to_anyone(firstname: str, lastname: str):
    """Say hello to anyone"""
    hello_message = f'Hello, {firstname.title()} {lastname.title()}!'
    return hello_message


def main(firstname: str, lastname: str, line_case: str):
    """Main controller"""
    if line_case == 'lower':
        hello_message = say_hello_to_anyone(firstname, lastname).lower()
    else:
        hello_message = say_hello_to_anyone(firstname, lastname).upper()
    print(hello_message)


if __name__ == '__main__':
    cli_args = parse_args()
    name = cli_args.first
    surname = cli_args.last
    case = cli_args.case
    main(name, surname, case)
