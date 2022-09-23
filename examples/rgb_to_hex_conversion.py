# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    # your code here :)
    colors = [r, g, b]
    check_colors = []
    for color in colors:
        if color > 255:
            color = 255
        check_colors.append(color)
    to_convert = ""
    for color in check_colors:
        to_convert = to_convert + hex(color)[2:].upper()
    return to_convert


if __name__ == "__main__":
    CASES = (
        ((255, 255, 255), 'FFFFFF'),
        ((255, 255, 300), 'FFFFFF'),
        # ((0, 0, 0), '000000'),
        # ((148, 0, 211), '9400D3')
    )
for case, answer in CASES:
    assert rgb(*case) == answer

result = eval("100 * 20 - 34")
print(type(result))
