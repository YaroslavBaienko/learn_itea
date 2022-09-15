"""
    Simple, given a string of words, return the length of the shortest word(s).
String will never be empty, and you do not need to account for different data types.
"""


def find_short(s):
    # your code here
    words = s.split()
    length = []
    for word in words:
        length.append(len(word))
    return min(length)


print(find_short('ABARAK bfr opfpdgswsw'))
