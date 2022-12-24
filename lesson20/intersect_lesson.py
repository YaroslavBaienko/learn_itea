import itertools
from typing import Iterable, Any, Hashable


def intersect_list_comprehension(iterable_one: Iterable[Any], iterable_two: Iterable[Any]):
    return [item for item in iterable_one if item in iterable_two]


class UnhashableType(Exception):
    pass


def check_hashable_items(iterable: Iterable[Any]):
    iterable_flat = itertools.chain.from_iterable(iterable)
    try:
        [hash(item) for item in iterable_flat]
    except TypeError as error:
        raise UnhashableType(error)


def intersect_sets(iterable_one: Iterable[Hashable], iterable_two: Iterable[Hashable]):
    check_hashable_items([item for item in (iterable_one, iterable_two)])
    return list(set(iterable_one) & set(iterable_two))


if __name__ == '__main__':
    iterable_first = [TypeError, 1, 'bob']
    iterable_second = [range, 1, 100.0, TypeError]

    intersect_set = intersect_sets(iterable_first, iterable_second)
    # intersect_comprehension = intersect_list_comprehension(iterable_first, iterable_second)

    print(intersect_set)
    # print(intersect_comprehension)

    # name_bob = 'bob'
    # name_bob1 = 'bob1'
    #
    # print(hash(name_bob))
    # print(hash(name_bob1))

