from accessify import private


class Point:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        if self.__check_coordinates(x, y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_coordinates(cls, x, y):
        return cls.MIN_COORDINATE <= x <= cls.MAX_COORDINATE and\
               cls.MIN_COORDINATE <= y <= cls.MAX_COORDINATE and\
               isinstance(x, int | float) and isinstance(y, int | float)

    def set_coordinates(self, x, y):
        if self.__check_coordinates(x, y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError(f'Type of agrs must be int or float and in range '
                             f'{self.MIN_COORDINATE} and {self.MAX_COORDINATE}')

    def get_coordinates(self):
        return f'X: {self.__x}, Y: {self.__y}'


if __name__ == '__main__':
    point = Point(10, 2)
    print(point.get_coordinates())
    # point.set_coordinates(1000, 4)
    print(dir(point))
    print(point._Point__check_coordinates(5, 6))
