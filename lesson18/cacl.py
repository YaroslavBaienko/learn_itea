class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if not x2:
            raise ZeroDivisionError('Incorrect value')
        return x1 / x2
