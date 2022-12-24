def some_func_list(items: list[int]):
    pass


def some_func_tuple(items: tuple[int, int, int]):
    pass


if __name__ == '__main__':
    test_tuple_data = (1, 2, 3)
    test_list_data = [1, 2, 3]

    some_func_list(test_list_data)
    some_func_tuple(test_tuple_data)
