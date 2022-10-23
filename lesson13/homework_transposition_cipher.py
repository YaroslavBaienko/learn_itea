"""Encrypt/decrypt transposition cipher"""
import math


def encrypt_message(key: int, message: str):
    """Encrypt transposition cipher"""
    ciphertext = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key
    return ''.join(ciphertext)


def decrypt_message(key: int, message: str):
    """Decrypt transposition cipher"""
    num_of_columns = int(math.ceil(len(message) / key))
    num_of_rows = key
    num_of_shaded_boxes = num_of_columns * num_of_rows - len(message)
    plaintext = [''] * num_of_columns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        first_condition = column == num_of_columns
        second_condition = column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes
        if first_condition or second_condition:
            column = 0
            row += 1
    return ''.join(plaintext)


def main(message: str, key: int, crypt: str):
    """Main controller"""
    result = False
    if crypt == 'encrypt':
        result = encrypt_message(key, message)
    elif crypt == 'decrypt':
        result = decrypt_message(key, message)
    return result


if __name__ == '__main__':
    my_message = """Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer."""
    my_key = 13
    my_encrypted_message = main(my_message, my_key, 'encrypt')
    my_decrypted_message = main(my_encrypted_message, my_key, 'decrypt')
    print(my_encrypted_message)
    print(my_decrypted_message)
