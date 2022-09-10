# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.


def sum_mix(arr):
    # your code here
    result = 0
    for num in arr:
        result = result + int(num)

    return result
