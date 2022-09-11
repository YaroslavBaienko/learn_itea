# Task

# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# Examples

# [7, 1] = >  [1, 7]
# [5, 8, 6, 3, 4] = >  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = >  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


def sort_array2(arr):
    odds = sorted([x for x in arr if x % 2 != 0], reverse=True)
    result = []
    for x in arr:
        if x % 2 == 0:
            result.append(x)
        else:
            result.append(odds.pop())
    return result


to_sort = [3, 2, 234, 5, 4, 9, 12, 1]
print(sort_array(to_sort))
print(sort_array2(to_sort))
