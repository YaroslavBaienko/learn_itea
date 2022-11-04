class Point:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORDINATE = left

    def __setattr__(self, key, value):
        print(f'__setattr__ key: {key} value: {value}')
        if key == 'a':
            raise AttributeError('Incorrect attr name')
        else:
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

    def __delattr__(self, item):
        print(f'__delattr__ {item}')
        object.__delattr__(self, item)


if __name__ == '__main__':
    point = Point(5, 20)
    # print(point.y)
    # del point.y
    # print(dir(point))
    # print(point.x)
    point.t = 37
    point.a = 25



