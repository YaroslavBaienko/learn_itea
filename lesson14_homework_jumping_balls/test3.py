import collections.abc
import math
import os


def floor(value,size,offset=200):
    return float(((value+offset)//size)*size-offset)

def path(filename):
    filepath=os.path.realpath(__file__)
    dirpath=os.path.dirname(filepath)
    fullpath=os.path.join(dirpath,filename)
    return fullpath

def line (a,b,x,y):
    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x, y)

def square (x,y,size,name):
    import turtle
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()



# Sequence requires data in a pair e.g. (3,5); collections.abc is an abstract class that vector is inheriting from
# that vector is inheriting from
class vector (collections.abc.Sequence):
# Precision sets the precision. Values are rounded to this precision.
    PRECISION=6
# __slots__ is a tuple with x,y co-ordinates and a hash field that decides if full or not. This not required.

#    __slots__=('_x','_y','_hash')

    def __init__(self,x,y):

# single underscore will prevent this variable from being imported by other modules
# _x and _y are the properly rounded x and y to 6 places internal variables while x and y are
# for the external world.

        self._x=round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)
        self._hash = None


# returns the x value which will be a copy of _x so v1.x will be v1._x

    @property
    #getter
    def x(self):
        return self._x

# sets the _x value as x(12)
    @x.setter
    def x(self,value):
        if self._hash is not None:
            raise ValueError("Cannot set x after hashing")
        self._x = round(value, self.PRECISION)

# returns the y value which will be a copy of _y
    # getter
    @property
    def y(self):
        return self._y

# sets the _y value as y(2)
    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set y after hashing")
        self._y = round(value, self.PRECISION)

# For a vector v, v.__hash checks if that location is free or occupied. v.x and v.y can only be set if
# __hash is empty.

    def __hash__(self):
        if self._hash is None:
# For a vector v, v.__hash__ is a function. If v is already (1,2) then if try v.x=2, then gives error
# pair is the tuple (3,5) for example
            pair=(self.x, self.y)
# pair is object. hash(object) is an in-built function and hash(pair) will return hash value
            self._hash = hash(pair)
        return self._hash


# __len__ is a method of abstract base class collections.Sequence and is being over-ridden here

    def __len__(self):
# Vector has two components (3,5) so it is has length 2.
        return 2

# __getitem__ is a method of abstract base class collections.Sequence and is being over-ridden here
# __getitem__ is getting individual components of the vector

    def __getitem__(self,index):
        if index==0:
            return self.x
        elif index==1:
            return self.y
        else:
            raise IndexError


# returns a copy of the vector object without the hash field
    def copy(self):
        type_self=type(self)
        return type_self(self.x,self.y)

# isinstance() function returns true if object other is of specified type (vector)
# __eq__ checks if self vector is equal to other vector (i.e. both x and y are equal). Will return True
# if they are equal

    def __eq__(self,other):
        if isinstance(other,vector):
            return self.x==other.x and self.y==other.y
        return NotImplemented

# __eq__ checks if self vector is equal to other vector (i.e. both x and y are equal). Will return True
# if they are not equal

    def __ne__(self,other):
        if isinstance(other,vector):
            return self.x!=other.x and self.y!=other.y
        return NotImplemented

# v.__iadd__(w) gives v+=w
# if self is a vector v(2,3) and other is also vector w(3,4) then __iadd__ gives v=(5,7)
# if self is a vector v(2,3) and other is a scalar e.g 3, then __iadd__ gives v=(5,6)
#
    def __iadd__(self,other):
        if self._hash is not None:
            raise ValueError ('Cannot add vector after hashing')
        elif isinstance(other,vector):
            self.x+=other.x
            self.y+=other.y
        else:
            self.x += other
            self.y += other
        return self

# v.__add__(w) gives v+w but v remains as it is.
# if self is a vector v(2,3) and other is also vector w(3,4) then __add__ gives vector=(5,7) but v still v(2,3)
# if self is a vector v(2,3) and other is a scalar e.g 3, then __add__ gives another vector v=(5,6) but v still v(2,3)

    def __add__(self, other):
        copy=self.copy()
        return copy.__iadd__(other)

    __radd__=__add__

# move vector by another
# if v=(1,2) and w=(3,4) then v.move(w) means move v by w so addition
    def move(self,other):
        self.__iadd__(other)

# if v=(1,2) v=v-w
    def __isub__(self,other):
        if self._hash is not None:
            raise ValueError('Cannot subtract vector after hashing')
        elif isinstance(other,vector):
            self.x-=other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

# v-w
    def __sub__(self,other):
        copy=self.copy()
        return copy.__isub__(other)

# v.__imul__(w) is v*=w
    def __imul__(self,other):
        if self._hash is not None:
            raise ValueError('Cannot multiply vector after hashing')
        elif isinstance(other,vector):
            self.x*=other.x
            self.y*= other.y
        else:
            self.x *= other
            self.y *= other
        return self

# v.__imul__(w) is v*w (1,2) x (3,4) = (3,8); 3* (1,2)=(3,6)
    def __mul__(self,other):
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self,other):
        self.__imul__(other)

# v.__itruediv__(w) is v/w
    def __itruediv__(self,other):
        if self._hash is not None:
            raise ValueError('Cannot divide vector after hashing')
        elif isinstance(other,vector):
            self.x/=other.x
            self.y/= other.y
        else:
            self.x /= other
            self.y /= other
        return self

# v.__itruediv__(w) is v/w
    def __truediv__(self,other):
        copy = self.copy()
        return copy.__itruediv__(other)

# (1,2) becomes (-1,-2)
    def __neg__(self):
        copy = self.copy()
        copy.x=-copy.x
        copy.y = -copy.y
        return copy

# (3,4) is 5
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

# x is xcos q - ysin q; y is ycos q +x sin q
    def rotate (self,angle):
        if self._hash is not None:
            raise ValueError('Cannot rotate vector after hashing')
        radians=angle*math.pi/180.0
        cosine=math.cos(radians)
        sine=math.sin(radians)

        x=self.x
        y=self.y

        self.x=x*cosine-y*sine
        self.y=y*cosine+x*sine

        return self

    def __repr__(self):
        type_self=type(self)
        name=type_self.__name__
        return '{} ({!r},{!r})'.format(name, self.x, self.y)


ant=vector(0,0.12345678)