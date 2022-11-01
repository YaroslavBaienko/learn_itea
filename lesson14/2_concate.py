from multipledispatch import dispatch


class Concatenate:
    max_x = 10
    max_y = 15

    @dispatch(float, float)
    def add(self, x, y):
        if x > self.max_x:
            x = self.max_x
        return x - y

    @dispatch(int, int)
    def add(self, x, y):
        return x + y


concatenator = Concatenate()
print(concatenator.add(1, 2))
print(concatenator.add(1.1, 0.5))
