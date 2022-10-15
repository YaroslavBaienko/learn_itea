def make_phone_map_keys(phone_interface: dict[str, tuple[str]]):
    phone_map_keys = {}
    for key, chars in phone_interface.items():
        char_codes = {char: key * index for index, char in enumerate(chars, 1)}
        phone_map_keys.update(char_codes)
    return phone_map_keys


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
    '0': (' ')
}


def check_key(phone_interface, key):
    if key not in phone_interface:
        return KeyError(f'{key} not in phone_interface')


def encode_to_phone(phone_map_keys, line):
    encode_message = ''
    for char in line:
        char = char.upper() if char.isalpha() else char
        check_key(phone_map_keys, char)
        encode_message += phone_map_keys[char] + '|'
    return encode_message[:-1]


def decode_to_text(phone_map_keys, codes_line):
    decode_message = ''
    codes_line = codes_line.split('|')
    inv_phone_map_keys = {code: char for char, code in phone_map_keys.items()}
    for code in codes_line:
        check_key(inv_phone_map_keys, code)
        decode_message += inv_phone_map_keys[code]
    return decode_message


def main(phone_interface, line, encode=True):
    phone_map_keys = make_phone_map_keys(phone_interface)
    print(phone_map_keys)
    if encode:
        result = encode_to_phone(phone_map_keys, line)
    else:
        result = decode_to_text(phone_map_keys, line)
    return result


if __name__ == '__main__':
    line1 = 'Hello world'
    phone_result = main(phone_interface=PHONE_INTERFACE, line=line1)
    text_result = main(PHONE_INTERFACE, phone_result, False)
    print(phone_result, text_result)
