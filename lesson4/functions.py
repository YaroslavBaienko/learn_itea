# def say_hello():
#     print('Hello!')
#
#
# say_hello()
# say_hello.__call__()
#
#
# def add(first, second):
#     return first + second
#
#
# print(add(2, 4))
#
#
# def first_func(x):
#     def second_func(y):
#         return x + y
#     return second_func
#
#
# sum_first = first_func(10)
# sum_second = sum_first(300)
# print(sum_second)


def find_average(a, b, c=[1, 2, 3]):
    if isinstance(c, list):
        return sum((a, b, *c)) / 3
    return sum((a, b, c)) / 3


# print(find_average(1, 2))
numbers = [1, 2, 3]
print(numbers)
print(*numbers)
print(find_average(1, 2, 3))


def make_something(*args, **kwargs):
    for num in args:
        print(num)
    for key in kwargs:
        print(key, kwargs[key])
    return args, kwargs


print(make_something(1, 2, 3, 4, 5, name='bob', last_name='smith'))
