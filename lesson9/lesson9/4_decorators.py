from datetime import datetime


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        data = func(*args, **kwargs)
        end = datetime.now()
        print(f'Time executed {func.__name__}(): {end - start}')
        print(f'Args positional {args}, kwargs: {kwargs}')
        return data
    return wrapper


@calc_time
def make_large_list(limit_pow, limit_size, now=1):
    return [x ** limit_pow for x in range(2 ** limit_size)]


numbers = make_large_list(32, 16, now=1)

names = ['bob', 'mike', 'rich']
# name_one, name_second, name_third = names

