class Point(object):
    """Class 2D point"""
    color = 'red'
    x = 30

    def __str__(self):
        return f'Color: {self.color}\nX: {self.x}'


a = Point()
b = Point()
print(Point.color, a.color, b.color)
print(a.__dict__)
print(Point.__dict__)
a.color = 'blue'
print(a.__dict__)
print(b.__dict__)
print(b.color)
Point.color = 'black'
print(b.color)
Point.shape = 'triangle'
print(a.shape)
setattr(Point, 'property', 25)
print(a.property)
print(getattr(a, 'property_', False))
print(Point.__doc__)
print(Point.__dict__)
del Point.property
print(hasattr(Point, 'property'))
delattr(Point, 'property')
