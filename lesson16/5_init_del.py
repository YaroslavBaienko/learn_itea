class Point:
    """Class 2D point"""
    color = 'red'
    shape = 'circle'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Delete instance of class Point {self}')

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point()
print(point.__dict__)
point.set_coordinates(10, 5)
print(point.get_coordinates())
