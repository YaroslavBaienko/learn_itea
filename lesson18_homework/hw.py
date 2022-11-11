"""Tests class Person"""
import unittest
from typing import NamedTuple
from lesson18_homework.person import Person


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        person_data = PersonData('Иванов Иван Иванович', 30, 'AA-123456', 100.0)
        self.person = Person(person_data)

    def tearDown(self) -> None:
        del self.person

    def test_full_name(self):
        self.assertEqual(self.person.full_name, 'Иванов Иван Иванович')

    def test_set_full_name(self):
        self.person.full_name = 'Петров Петр Петрович'
        self.assertEqual(self.person.full_name, 'Петров Петр Петрович')

    def test_verify_full_name(self):
        with self.assertRaises(TypeError) as error:
            self.person.full_name = 12
        self.assertEqual('Full name must be a string', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = ' '
        self.assertEqual('Full name must contain at least one character', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = 'Юлия Сергеевна'
        self.assertEqual('Invalid name format', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = '_ Юлия Сергеевна'
        self.assertEqual('Full name can only contain letter', error.exception.args[0])

    def test_age(self):
        self.assertEqual(self.person.age, 30)

    def test_set_age(self):
        self.person.age = 40
        self.assertEqual(self.person.age, 40)

    def test_verify_age(self):
        with self.assertRaises(TypeError):
            self.person.age = 99.0

        with self.assertRaises(ValueError):
            self.person.age = 10

    def test_id_card(self):
        self.assertEqual(self.person.id_card, 'AA-123456')

    def test_set_id_card(self):
        self.person.id_card = 'ZZ-654321'
        self.assertEqual(self.person.id_card, 'ZZ-654321')

    def test_verify_id_card(self):
        with self.assertRaises(TypeError):
            self.person.id_card = 12

        with self.assertRaises(ValueError):
            self.person.id_card = 'KK654321'

    def test_weight(self):
        self.assertEqual(self.person.weight, 100.0)

    def test_set_weight(self):
        self.person.weight = 90.0
        self.assertEqual(self.person.weight, 90.0)

    def test_verify_weight(self):
        with self.assertRaises(TypeError):
            self.person.weight = 65

        with self.assertRaises(ValueError):
            self.person.weight = 150.0

    def test__str__(self):
        self.assertEqual(self.person.__str__(), 'Иванов Иван Иванович')


if __name__ == '__main__':
    unittest.main()