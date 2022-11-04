class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        print('__call__')
        if not isinstance(args[0], str):
            raise TypeError('Arg must be string')
        self.__counter += 1
        return args[0].strip(self.__chars)


if __name__ == '__main__':
    strip1 = StripChars('?:;.,!')
    strip2 = StripChars(' ')
    result1 = strip1('?Hello, world!')
    result2 = strip2('   ?Hello, world!   ')
    print(result1)
    print(result2)

