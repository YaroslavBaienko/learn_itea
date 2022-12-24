import pytest
import warnings
import numpy as np


def math_func_mean(items):
    print(f'The mean is {np.mean(items)}')


def math_func_max(items):
    print(f'The mean is {np.max(items)}')


def main(items):
    if len(items) < 3:
        warnings.warn('Too small list')

    if not isinstance(items, list):
        raise TypeError('Type must be a list')

    math_func_mean(items)
    math_func_max(items)


class TestMathOperations:
    def setup_method(self):
        self.data = [1, 2, 3, 4, 5]
        self.func = main

    def teardown_method(self):
        del self.func

    def test_main(self, capfd):
        self.func(self.data)
        assert capfd.readouterr().out == f'The mean is {np.mean(self.data)}\nThe mean is {np.max(self.data)}\n'

    def test_main_with_wrong_type(self):
        with pytest.raises(TypeError) as context:
            self.func((1, 2, 3))
        assert 'Type must be a list' == str(context.value)

    def test_main_with_small_value(self):
        with pytest.warns(Warning, match='Too small list'):
            self.func([1, 2])


assert '1' in '123'
assert '123' == '123'
assert '1' != '123'

variable = bool([1, 2, 3])
assert variable

