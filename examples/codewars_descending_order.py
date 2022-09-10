# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number. Examples:
#
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321
def descending_order(num):
    # Bust a move right here
    num = str(num)
    clearlist = []
    for digit in num:
        clearlist.append(digit)
    clearlist = clearlist[::-1]
    clearlist.sort(reverse=True)
    result = int("".join(clearlist))
    return result


print(descending_order(7476898301))
