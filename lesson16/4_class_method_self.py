class Point(object):
    """Class 2D point"""
    color = 'red'
    shape = 'circle'

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point()
print(point.__dict__)
point.set_coordinates(5, 10)
print(point.__dict__)
if getattr(point, 'r', False):
    setattr(point, 'r', 10)
print(point.get_coordinates())
