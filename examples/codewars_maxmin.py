# Story
#
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give
# him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the
# lowest possible price and sell it at the highest. Task
#
# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    maximum = max(lst)
    minimum = min(lst)
    result = list()
    result.append(minimum)
    result.append(maximum)
    return result


print(min_max([1, 2, - 10, 34]))
