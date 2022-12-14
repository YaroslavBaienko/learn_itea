import unittest



class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo1'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.islower())


    def test_split(self):
        welcome = 'hello world'
        self.assertEqual(welcome.split(' '), ['hello', 'world'])

        with self.assertRaises(TypeError):
            welcome.split(2)



if __name__ == '__main__':
    unittest.main()
    test1 = TestStringMethods.test_split()