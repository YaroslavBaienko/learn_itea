def first(num1):
    var = 10

    def second(num2):
        return num1 + num2 + var

    return second


func = first(2)

func.name = 'wrapper'

result = func(3)
print(result)


def mult():
    return 2 * 2


mult.name = 'bob'
mult()
print(mult.name)
