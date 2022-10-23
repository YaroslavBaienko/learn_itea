import math


def encrypt_using_vertical_cipher(key: str, message: str) -> str:
    message = message.replace(' ', '*')
    key_chars = [x for x in key]
    key_length = len(key)
    message_length = len(message)
    chars_count = message_length % key_length

    if chars_count != 0:
        message = message + ((key_length - chars_count) * "*")

    rows_count = int(math.ceil(message_length / key_length))
    key_row = []

    for i in range(0, rows_count):
        key_row.append(key_chars[i % key_length])

    s = 0
    m = 0
    n = 0
    messages = {}
    sum_of_rows = {}
    new = []
    for k in key_row:
        n += 1
        t = 0
        rows_map = {}
        for symbol in message[s: s + key_length]:
            rows_map[key_chars[t]] = symbol
            t += 1

        sum_of_rows[k] = rows_map.copy()
        if len(sum_of_rows) == key_length or len(key_row) == n:
            new.append(sum_of_rows)
            messages[m] = sum_of_rows.copy()
            sum_of_rows.clear()
            m += 1

        s += key_length

    for u in messages:
        for v in messages[u]:
            messages[u][v] = sorted(messages[u][v].items(), key=lambda kv: (kv[0], kv[1]))

    encrypted_text = ""
    for i in range(0, key_length):
        for g in messages:
            for h in messages[g]:
                encrypted_text += messages[g][h][i][1]

    return encrypted_text


def decrypt_from_vertical_cipher_text(key: str, cipher: str) -> str:
    cipher_length = len(cipher)
    cipher_chars = [x for x in cipher]
    key_length = len(key)
    rows_count = int(math.ceil(cipher_length / key_length))
    sorted_key_chars = sorted([x for x in key])
    matrix = []
    for _ in range(rows_count):
        matrix += [[None] * key_length]
    k = 0
    i = 0
    for _ in range(key_length):
        m = key.index(sorted_key_chars[k])

        for j in range(rows_count):
            matrix[j][m] = cipher_chars[i]
            i += 1
        k += 1

    decrypted_text = ""
    for s in range(0, rows_count):
        for t in range(0, key_length):
            decrypted_text += matrix[s][t]

    return decrypted_text


def main():
    message = input("Please, write text would you like to encrypt: ").upper()
    key = input("Choose your key subsequence such as '645312', etc. : ").upper()
    encrypted_text = encrypt_using_vertical_cipher(key, message)
    decrypted_text = decrypt_from_vertical_cipher_text(key, encrypted_text)
    print(f'Encrypted text is: {encrypted_text} which decrypted looks like: {decrypted_text}')


if __name__ == '__main__':
    main()
