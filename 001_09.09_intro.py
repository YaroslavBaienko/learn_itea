import sys

print("Hello, world!")
a = b = [1, 2, 3, 4, 5, 6]
print(id(a), id(b))
print(sys.getrefcount(a))

print(sys.getsizeof(a))
