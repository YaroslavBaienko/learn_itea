# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
# Example
#
# alphabet_position("The sunset sets at twelve o' clock.")
#
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
def alphabet_position(text):
    import string
    alphabet = string.ascii_lowercase
    all_letters = list(alphabet)
    text = text.lower()

    sentence_letters = [letter for letter in text]

    alphabet_dictionary = {}

    value = 0
    for key in all_letters:
        value += 1
        alphabet_dictionary[key] = str(value)

    print(alphabet_dictionary)

    result = []
    for letter in sentence_letters:
        if letter in all_letters:
            result.append(alphabet_dictionary[letter])
        else:
            continue

    result = " ".join(result)
    return result


print(alphabet_position("hghj hjg hjghj g8776768"))
