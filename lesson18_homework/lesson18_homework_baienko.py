import unittest
from typing import NamedTuple
from lesson18_homework.person import Person, PersonData, PersonVerify


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        person_data = PersonData('Степанов Петр Степанович', 40, 'ВР-576844', 69.0)
        self.person = Person(person_data)

    def tearDown(self) -> None:
        del self.person

    def test_full_name(self):
        self.assertEqual(self.person.full_name, 'Степанов Петр Степанович')

    def test_set_full_name(self):
        self.person.full_name = 'Гольдштейн Иммануил Иосифович'
        self.assertEqual(self.person.full_name, 'Гольдштейн Иммануил Иосифович')

    def test_verify_full_name(self):
        with self.assertRaises(TypeError) as error:
            self.person.full_name = 12
        self.assertEqual('Full name must be a string', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = ' '
        self.assertEqual('Full name must contain at least one character', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = 'Исаак Семенович'
        self.assertEqual('Invalid name format', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = '!%; Исаак Семенович'
        self.assertEqual('Full name can only contain letter', error.exception.args[0])

    def test_age(self):
        self.assertEqual(self.person.age, 21)

    def test_set_age(self):
        self.person.age = 40
        self.assertEqual(self.person.age, 54)

    def test_verify_age(self):
        with self.assertRaises(TypeError):
            self.person.age = 95.0

        with self.assertRaises(ValueError):
            self.person.age = 9

    def test_id_card(self):
        self.assertEqual(self.person.id_card, 'ВР-576844')

    def test_set_id_card(self):
        self.person.id_card = 'SQ-475847'
        self.assertEqual(self.person.id_card, 'ZZ-654321')

    def test_verify_id_card(self):
        with self.assertRaises(TypeError):
            self.person.id_card = 12

        with self.assertRaises(ValueError):
            self.person.id_card = 'ВР279765'

    def test_weight(self):
        self.assertEqual(self.person.weight, 115.0)

    def test_set_weight(self):
        self.person.weight = 90.0
        self.assertEqual(self.person.weight, 80.0)

    def test_verify_weight(self):
        with self.assertRaises(TypeError):
            self.person.weight = 64

        with self.assertRaises(ValueError):
            self.person.weight = 190.0

    def test__str__(self):
        self.assertEqual(self.person.__str__(), 'Иванов Иван Иванович')


if __name__ == '__main__':
    unittest.main()
