def multiply(num1):
    var = 10

    def inner(num2):
        return num1 + num2 + var

    return inner


func = multiply(2)
result = func(3)
print(result)


def mult():
    return 2 * 2

mult.name = 'bob'
print(mult.name)