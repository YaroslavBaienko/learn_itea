"""Encode, decode old phone interface messages"""


def make_phone_map_keys(phone_interface: dict[str, tuple[str]]):
    """Make an expand structure of the phone's keys"""
    phone_map_keys = {}
    for key, chars in phone_interface.items():
        char_codes = {char: key * index for index, char in enumerate(chars, 1)}
        phone_map_keys.update(char_codes)
    return phone_map_keys


def check_key(phone_interface: dict[str, tuple[str]], key: str):
    """Check if key in PHONE_INTERFACE"""
    if key not in phone_interface:
        raise KeyError(f'{key} not in PHONE_INTERFACE')


def encode_to_phone(phone_map_keys: dict[str, tuple[str]], message: str):
    """Encode message to phone codes"""
    encode_message = ''
    for char in message:
        char = char.upper() if char.isalpha() else char
        check_key(phone_map_keys, char)
        encode_message += phone_map_keys[char] + '|'
    return encode_message[:-1]


def decode_to_phone(phone_map_keys: dict[str, tuple[str]], codes_line: str):
    """Decode phone code to message"""
    decode_message = ''
    codes_line = codes_line.split('|')
    inv_phone_map_keys = {code: char for char, code in phone_map_keys.items()}
    for code in codes_line:
        check_key(inv_phone_map_keys, code)
        decode_message += inv_phone_map_keys[code]
    return decode_message


def main(phone_interface: dict[str, tuple[str]], line: str, encode=True):
    """Main controller"""
    phone_map_keys = make_phone_map_keys(phone_interface)
    if encode:
        result = encode_to_phone(phone_map_keys, line)
    else:
        result = decode_to_phone(phone_map_keys, line)
    return result


PHONE_INTERFACE = {
    '1': ('.', ',', '?', '!', ':'),
    '2': ('A', 'B', 'C'),
    '3': ('D', 'E', 'F'),
    '4': ('G', 'H', 'I'),
    '5': ('J', 'K', 'L'),
    '6': ('M', 'N', 'O'),
    '7': ('P', 'Q', 'R', 'S'),
    '8': ('T', 'U', 'V'),
    '9': ('W', 'X', 'Y', 'Z'),
    '0': (' ',)
}
