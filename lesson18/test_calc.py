import unittest
from lesson18.cacl import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        del self.calculator

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(2, 0)


if __name__ == '__main__':
    unittest.main()
