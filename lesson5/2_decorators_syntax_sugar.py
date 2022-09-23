def verbose(func):
    def wrapper(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@verbose
def upper(string):
    return string.upper()


@verbose
def lower(string):
    return string.lower()


@verbose
def capitalize(string):
    return string.capitalize()


full_name = 'Joe Doe'

upper(full_name)
lower(full_name)
capitalize(full_name)
