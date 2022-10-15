"""Program that encode sentence using Ceasar's code and decode it"""
import string
import argparse
from argparse import Namespace


def parse_args() -> Namespace:
    """Parse args with argparse"""
    parser = argparse.ArgumentParser(
        prog='main',
        usage='%(prog)s lesson11_homework_baienko.py --message <message> --lang <language> --shift <shift> [--param encode|decode]',
        description='Encrypt or decrypt message using Ceasar code'
    )
    parser.add_argument(
        '-m',
        '--message',
        type=str,
        help='enter message would you like to encrypt/decrypt',
        required=True
    )
    parser.add_argument(
        '-l',
        '--language',
        type=str,
        help='enter language EN or UA',
        required=True
    )
    parser.add_argument(
        '-s',
        '--shift',
        type=int,
        help='enter shifting position',
        required=True
    )
    parser.add_argument(
        '-e'
        '--encode',
        type=str,
        help='choose encoding mode',
        required=False
    )
    parser.add_argument(
        '-d'
        '--decode',
        type=str,
        help='choose decoding mode',
        required=False
    )
    args = parser.parse_args()
    return args


def encode_to_ceasar_code(map_keys: dict[str:str], message: str) -> str:
    """Encode message using Ceasar code"""
    encode_message = ''
    for char in message:
        if char.isalpha():
            char = char.upper()
            encode_message += map_keys[char]
        else:
            encode_message += char
    return encode_message


def make_ceasar_map_keys(shift: int, alphabet: str) -> dict[str:str]:
    """Make an expand structure of the ceasars code keys"""
    # alphabet = string.ascii_uppercase
    map_keys = {}
    for pos, letter in enumerate(alphabet):
        shifting = pos + shift
        if shifting < len(alphabet):
            map_keys[letter] = alphabet[shifting]
        else:
            map_keys[letter] = alphabet[shifting - len(alphabet)]
    return map_keys


def decode_from_ceasar_code(map_keys: dict[str:str], encoded_message: str) -> str:
    """Encode message using Ceasar code"""
    decode_message = ''
    inv_map_keys = {code: char for char, code in map_keys.items()}
    for code in encoded_message.upper():
        if code in map_keys:
            decode_message += inv_map_keys[code]
        else:
            decode_message += code
    return decode_message


def main(language, line, shift: int, encode: True):
    """Main controller"""
    codes = make_ceasar_map_keys(shift=shift, alphabet=language)
    if encode:
        result = encode_to_ceasar_code(map_keys=codes, message=line)
    else:
        result = decode_from_ceasar_code(map_keys=codes, encoded_message=line)
    return result


ALPHABET_UA = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
ALPHABET_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == '__main__':
    cli_args = parse_args()
    message = cli_args.message
    alpha = cli_args.language
    shifting = cli_args.shift
    try:
        print(main(language=alpha, line=message, shift=shifting, encode=True))
    except KeyError as error:
        print('Use symbols from current alphabet')
    # message_to_encrypt = 'Hello world'
    # message_to_decrypt = 'JGNNQ YQTNF'
    # shift = 2
    # print(main(language=ALPHABET_EN, line=message_to_encrypt, shift=shift, encode=True))
    # print(main(language=ALPHABET_EN, line=message_to_decrypt, shift=shift, encode=False))
