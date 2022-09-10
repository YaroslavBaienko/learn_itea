class TestClass:
    def __init__(self):
        pass

    version = 1


test1 = TestClass()
test2 = TestClass()
test3 = test1

print(id(test1), id(test2), id(test3))
