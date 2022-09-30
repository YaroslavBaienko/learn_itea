"""Calc execution time"""
from datetime import datetime


def calc_time(func):
    """Calc execution time"""
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func_result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f'Execution time {func.__name__}: {end_time - start_time}')
        return func_result
    return wrapper
