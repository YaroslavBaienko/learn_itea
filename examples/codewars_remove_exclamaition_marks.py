# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    # your code here
    result = []
    for letter in s:
        if letter == "!":
            continue
        else:
            result.append(letter)
    return "".join(result)


print(remove_exclamation_marks("Hello! world!"))
