def getCipher(origin_key, origin_text):
    clear_text = ''.join(origin_text.split(' ')).lower()
    k = len(clear_text) // len(origin_key)

    cipher = {}
    for index, ch in enumerate(origin_key.lower()):
        if ch in cipher:
            cipher[ch] += clear_text[index * k : index * k + k]
        else:
            cipher[ch] = clear_text[index * k : index * k + k]

    cipher_text = ''.join([''.join([cipher[key][index] for key in sorted(cipher.keys())]) for index in range(k)])
    return ' '.join([cipher_text[index : index + k] for index in range(0, len(cipher_text), k)]).upper()


print(getCipher('ПЕЛИКАН', 'ТЕРМИНАТОР ПРИБЫВАЕТ СЕДЬМОГО В ПОЛНОЧЬ'))