from caesar_cipher import CHARS


def hack_caesar_cipher(message: str):
    """Iterates over all possible options"""
    for key in range(len(CHARS)):
        translated_text = ''
        for char in message:
            if char in CHARS:
                char_index = CHARS.find(char)
                translated_index = char_index - key
                if translated_index < 0:
                    translated_index += len(CHARS)
                translated_text += CHARS[translated_index]
            else:
                translated_text += char
        print(f'Key #{key}: {translated_text}')


if __name__ == '__main__':
    decrypt_message = 'guv5Mv5Mz"M5rp4r6Mzr55ntr_'
    hack_caesar_cipher(decrypt_message)
