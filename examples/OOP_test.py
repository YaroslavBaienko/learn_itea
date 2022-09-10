class TestClass:
    def __init__(self):
        pass

    version = 1


TestClass.version = 24
test1 = TestClass()
test2 = TestClass()
test3 = test1
test2.version = 100


print(id(test1.version), id(test2.version), id(test3.version))

print(test1.version)
