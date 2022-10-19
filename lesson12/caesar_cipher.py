import pyperclip
from string import (
    ascii_uppercase,
    ascii_lowercase,
    digits,
    punctuation,
    whitespace
)


def encrypt_message(message: str, shift: int, chars: str):
    """Encrypt message using Caesar cipher"""
    translated_text = ''
    for char in message:
        if char in chars:
            char_index = chars.find(char)
            translated_index = char_index + shift
            if translated_index >= len(CHARS):
                translated_index -= len(CHARS)
            translated_text += CHARS[translated_index]
        else:
            translated_text += char
    return translated_text


def decrypt_message(message, shift, chars):
    """Decrypt message using Caesar cipher"""
    translated_text = ''
    for char in message:
        if char in chars:
            char_index = chars.find(char)
            translated_index = char_index - shift
            if translated_index < 0:
                translated_index = translated_index + len(CHARS)
            translated_text += CHARS[translated_index]
        else:
            translated_text += char
    return translated_text


def main(message: str, shift: int, chars: str, mode: str):
    """Main controller"""
    result = False
    if mode == 'encrypt':
        result = encrypt_message(message, shift, chars)
    elif mode == 'decrypt':
        result = decrypt_message(message, shift, chars)
    return result


CHARS = ascii_uppercase + ascii_lowercase + digits + punctuation + ' '

if __name__ == '__main__':
    test_message = 'This is my secret message.'
    test_text_key = 13
    mode_encrypt = 'encrypt'

    encrypt_text = main(test_message, test_text_key, CHARS, 'encrypt')
    print(f'Encrypt text: {encrypt_text}')
    pyperclip.copy(encrypt_text)

    decrypt_text = main(encrypt_text, test_text_key, CHARS, 'decrypt')
    print(f'Decrypt text: {decrypt_text}')
