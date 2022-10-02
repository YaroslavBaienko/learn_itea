import string
import random
from datetime import datetime


def password_generator(letters: int, numbers: int):
    chars = [random.choice(string.ascii_letters) for i in range(letters)]
    digits = [random.choice(string.digits) for i in range(numbers)]
    chars.extend(digits)
    random.shuffle(chars)
    return "".join(chars)


def time_to_find_passwd(letters: int, numbers: int):
    start_time = datetime.now()
    while True:
        passwd = password_generator(letters, numbers)
        passwd2 = password_generator(letters, numbers)
        if passwd == passwd2:
            print(f'Password found: {passwd} = {passwd2}')
            end_time = datetime.now() - start_time
            print(f'We are need {end_time} to find password that contain {len(passwd)} characters')
            break


if __name__ == '__main__':
    time_to_find_passwd(0, 8)
