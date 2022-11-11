import unittest


def add_fish_to_aquarium(fish_list: list[str]):
    if len(fish_list) > 10:
        raise ValueError('A maximum of 10 fish can be added to the aquarium')
    return {'tank': fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def setUp(self) -> None:
        self.func = add_fish_to_aquarium

    def test_add_aquarium_success(self):
        actual = self.func(fish_list=['shark', 'tuna'])
        expected = {'tank': ['shark', 'tuna']}
        self.assertEqual(actual, expected)

    def test_add_aquarium_wrong(self):
        actual = self.func(fish_list=['shark', 'tuna'])
        expected = {'tank': ['shark']}
        self.assertNotEqual(actual, expected)

    def test_add_aquarium_exception_max_fish(self):
        too_many_fish = ['shark'] * 25

        with self.assertRaises(ValueError) as exception_max_fish_context:
            self.func(too_many_fish)

        self.assertEqual(
            str(exception_max_fish_context.exception),
            'A maximum of 10 fish can be added to the aquarium'
        )


if __name__ == '__main__':
    unittest.main()

