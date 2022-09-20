# def add(first, second):
#     first + second
#
# print(add(2, 2))
#
#
# def first_func(x):
#     def second_func(y):
#         return x + y
#     return second_func
#
#
# sum_first = first_func(100)(200)
# print(sum_first)
#


# def find_average(a, b, c=[1, 2, 3]):
#     if isinstance(c, list):
#         return sum((a, b, *c)) / 3
#     return sum((a, b, c)) / 3
#
#
# print(find_average(1, 2, 3))
# numbers = [1, 2, 3]
# # print(numbers)
# # print(*numbers)

def make_something(*args, **kwargs):
    for num in args:
        print(num)
    for key in kwargs:
        print(key, kwargs[key])
    return args, kwargs


print(make_something(1, 2, 3, 4, name='bob', last_name='smith'))

func_title = lambda value: value.title()
print(func_title('new'))

func_add = lambda a, b: a + b
print(func_add(2, 3))
