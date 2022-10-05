"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string


def is_pangram(s):
    pangrams = list()
    clear = list()
    to_compare = 'abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if letter in string.ascii_letters:
            pangrams.append(letter.lower())
        for item in pangrams:
            if item not in clear:
                clear.append(item)
        clear = sorted(clear)
        str_pangr = ''.join(clear)
        if str_pangr == to_compare:
            return True
    return False


s = 'The quick brown fox jumps over the lazy dog'
print(is_pangram(s=s))
