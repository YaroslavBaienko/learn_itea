"""Delete comments form code files"""
import argparse

from decorators.calc_execution_time import calc_time


def parse_ars():
    """Parse CLI args"""
    parser = argparse.ArgumentParser(
        prog='Delete comments',
        usage='%(prog)s delete_comments.py --input <filename> [--output <filename>]',
        description='Delete comments form code files'
    )
    parser.add_argument(
        '--input',
        type=str,
        help='path to source code file',
        required=True
    )
    parser.add_argument(
        '--output',
        type=str,
        help='path to destination file',
        required=False,
        default='clean_code_out.py'
    )
    args = parser.parse_args()
    return args


def check_exist_type_file(filename: str):
    """Check FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def normalize_code_line(line: str):
    """Normalize code lines include char_to_delete"""
    char_to_delete = '#'
    if line.strip().startswith(char_to_delete):
        return ''

    if char_to_delete in line:
        char_index = line.index(char_to_delete)
        line = line[:char_index] + '\n'
    return line


def read_code_from_file(filename: str):
    """Read code from .py files"""
    normalized_code = []
    with open(filename) as code_file:
        for line in code_file:
            normalized_line = normalize_code_line(line)
            if normalized_line:
                normalized_code.append(normalized_line)
    return normalized_code


@calc_time
def write_code_to_file(filename: str, codes):
    """Write clean code to file"""
    with open(filename, 'w') as code_file:
        for code_line in codes:
            code_file.write(code_line)
    return True


@calc_time
def main(input_file: str, output_file: str):
    """Main controller"""
    check = check_exist_type_file(input_file)
    if check:
        print(check)
        exit()
    clean_code = read_code_from_file(input_file)
    if write_code_to_file(output_file, clean_code):
        print(f'Normalized code from {input_file} to {output_file}')


if __name__ == '__main__':
    cli_args = parse_ars()
    input_file = cli_args.input
    output_file = cli_args.output

    main(input_file, output_file)

