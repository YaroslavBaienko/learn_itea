"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
function should return true if the string is valid, and false if it's invalid. Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore,
the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).

"""


def valid_parentheses(phrase):
    import string
    parentheses = []
    for symbol in phrase:
        if (symbol == string.punctuation[7]) or (symbol == string.punctuation[8]):
            parentheses.append(symbol)
    right = 0
    left = 0

    for parent in parentheses:
        if parent == string.punctuation[7]:
            right += 1
        else:
            left += 1
    parent_phrase = "".join(parentheses)
    if right == left and ")(" not in parent_phrase:
        return True
    else:
        return False


print(valid_parentheses("hi())("))
