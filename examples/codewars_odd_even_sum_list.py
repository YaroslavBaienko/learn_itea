# Given a list of integers, determine whether the sum of its elements is odd or even.
#
# Give your answer as a string matching "odd" or "even".
#
# If the input array is empty consider it as: [0] (array with a zero).
def odd_or_even(arr):
    sum = 0
    for num in arr:
        sum = sum + num

    if sum % 2:
        return "odd"
    else:
        return "even"


print(odd_or_even([2, -45, 2, 10]))
