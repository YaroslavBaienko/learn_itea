def sort(x):
    z = lambda y: sorted(filter(y, x))
    return ''.join(z(str.isalpha) + z(str.isdigit))


print(sort('sdfsfd34rfef30945'))
