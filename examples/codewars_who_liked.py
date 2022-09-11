# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the
# display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    # your code here
    result = ""

    if len(names) == 2:
        result = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        result = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) == 0:
        result = "no one likes this"
    elif len(names) == 1:
        result = f"{names[0]} likes this"
    else:
        count = 0
        for name in names[2:]:
            count = count + 1
        result = f"{names[0]}, {names[1]} and {count} others like this"

    return result


print(likes([]))
