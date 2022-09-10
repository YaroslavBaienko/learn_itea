# Your
# task is to
# make
# two
# functions(max and min, or maximum and minimum, etc., depending
# on
# the
# language ) that
# receive
# a
# list
# of
# integers as input, and return the
# largest and lowest
# number in that
# list, respectively.
def maximum(arr):
    maxim = arr[0]
    for num in arr:
        if num > maxim:
            maxim = num
    return maxim


def minimum(arr):
    minim = arr[0]
    for num in arr:
        if num < minim:
            minim = num
    return minim


print(minimum([-1, -200, 0, 20, -300]))
# ...and here
