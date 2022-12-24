import unittest

from person.person import Person, PersonData


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.data = PersonData('Иванов Иван Иванович', 36, 'ВР-415141', 101.3)
        self.person = Person(self.data)

    def tearDown(self) -> None:
        del self.person

    def test_normal_data(self):
        self.assertEqual(self.person.full_name, self.data.full_name)
        self.assertEqual(self.person.age, self.data.age)
        self.assertEqual(self.person.id_card, self.data.id_card)
        self.assertEqual(self.person.weight, self.data.weight)

    def test_set_values(self):
        self.person.full_name = 'Петров Петр Петрович'
        self.person.age = 41
        self.person.id_card = 'АР-787912'
        self.person.weight = 66.0

        self.assertEqual(self.person.full_name, 'Петров Петр Петрович')
        self.assertEqual(self.person.age, 41)
        self.assertEqual(self.person.id_card, 'АР-787912')
        self.assertEqual(self.person.weight, 66.0)

        self.reset_person()

    def test_set_en_values(self):
        self.person.full_name = 'John Richard McLain'
        self.person.age = 25
        self.person.id_card = 'RG-787912'
        self.person.weight = 97.8

        self.assertEqual(self.person.full_name, 'John Richard McLain')
        self.assertEqual(self.person.age, 25)
        self.assertEqual(self.person.id_card, 'RG-787912')
        self.assertEqual(self.person.weight, 97.8)

        self.reset_person()

    def test_with_wrong_full_name(self):
        with self.assertRaises(TypeError) as context_not_string:
            self.person.full_name = 200
        self.assertTrue('Full name must be a string' in str(context_not_string.exception))

        with self.assertRaises(TypeError) as context_wrong_length:
            self.person.full_name = 'bob'
        self.assertTrue('Invalid name format' in str(context_wrong_length.exception))

        with self.assertRaises(TypeError) as context_empty_value:
            self.person.full_name = ' '
        self.assertTrue('Full name must contain at least one character' in str(context_empty_value.exception))

        with self.assertRaises(TypeError) as context_digits_value:
            self.person.full_name = '7 7 7'
        self.assertTrue('Full name can only contain letters' in str(context_digits_value.exception))

    def test_with_wrong_age(self):
        with self.assertRaises(ValueError) as context_value_max:
            self.person.age = 200
        self.assertTrue('Age must be between' in str(context_value_max.exception))

        with self.assertRaises(ValueError) as context_value_min:
            self.person.age = 10
        self.assertTrue('Age must be between' in str(context_value_min.exception))

        with self.assertRaises(TypeError) as context_type:
            self.person.age = 20.5
        self.assertTrue('Age must be an integer' == str(context_type.exception))

    def test_with_wrong_weight(self):
        with self.assertRaises(TypeError) as context_type:
            self.person.weight = 100
        self.assertEqual('Weight must be an float number', str(context_type.exception))

        with self.assertRaises(ValueError) as context_value_max:
            self.person.weight = 200.0
        self.assertTrue('Weight should be between' in str(context_value_max.exception))

        with self.assertRaises(ValueError) as context_value_min:
            self.person.weight = 10.0
        self.assertTrue('Weight should be between' in str(context_value_min.exception))

    def test_with_wrong_id_card(self):
        with self.assertRaises(TypeError) as context_type:
            self.person.id_card = None
        self.assertEqual('Invalid data type for card id', str(context_type.exception))

        with self.assertRaises(ValueError) as context_value:
            self.person.id_card = 'id777777'
        self.assertEqual('Invalid card id data format XX-XXXXXX', str(context_value.exception))

    def reset_person(self):
        self.person = Person(self.data)
