class Vector:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    @classmethod
    def validate_coordinates(cls, arg):
        return cls.MIN_COORDINATE <= arg <= cls.MAX_COORDINATE

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate_coordinates(x) and self.validate_coordinates(y):
            self.x = x
            self.y = y

    def get_coordinates(self):
        return self.x, self.y

    @staticmethod
    def quadratic_form(x, y):
        return x * x + y * y


if __name__ == '__main__':
    vector = Vector(2, 3)
    print(vector.get_coordinates())
    print(Vector.quadratic_form(2, 3))
    print(vector.quadratic_form(*vector.get_coordinates()))
