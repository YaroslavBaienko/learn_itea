import io
import unittest
from unittest.mock import patch

from database.db import DataBase, DataBaseDTO, DataBaseException


class TestDataBase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        self.database = DataBase(self.data)
        print(' ' * 20 + f'***{self._testMethodName}***')

    def tearDown(self) -> None:
        del self.data
        del self.database

    def test_init_database_correct_data(self):
        self.assertEqual(self.data.db_name, self.database.db_name)
        self.assertEqual(self.data.user, self.database.user)
        self.assertEqual(self.data.password, self.database.password)
        self.assertEqual(self.data.host, self.database.host)
        self.assertEqual(self.data.port, self.database.port)

    def test_delete_database_instance(self):
        self.database.__del__()
        self.assertEqual(DataBase.instance(), None)

    def test_singleton_database_pattern(self):
        data_mysql = DataBaseDTO('mysql', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        data_postgres = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')

        database_mysql = DataBase(data_mysql)
        database_postgres = DataBase(data_postgres)

        self.assertEqual(id(database_mysql), id(database_postgres))

    def test_connect_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database.connect()
        self.assertEqual(fake_out.getvalue(), f'Connect to DB: {self.data.db_name}\n')

    def test_close_connect_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database.close()
        self.assertEqual(fake_out.getvalue(), f'Close connect to DB: {self.database.db_name}\n')

    def test_read_from_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database.read('Owner')
        self.assertEqual(fake_out.getvalue(), f'Read data from database: '
                                              f'{self.database.db_name} from table: Owner\n')

    def test_write_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database.write('Owner', 'Some value')
        self.assertEqual(fake_out.getvalue(), f'Write Some value to DB: {self.database.db_name} table: Owner\n')

    def test_set_correct_db_name(self):
        self.database.db_name = 'mysql'
        self.assertEqual(self.database.db_name, 'mysql')

    def test_set_correct_user(self):
        self.database.user = 'user'
        self.assertEqual(self.database.user, 'user')

    def test_set_correct_password(self):
        self.database.password = 'user777U!'
        self.assertEqual(self.database.password, 'user777U!')

    def test_set_correct_host(self):
        self.database.host = '8.8.8.8'
        self.assertEqual(self.database.host, '8.8.8.8')

    def test_set_correct_port(self):
        self.database.port = '5000'
        self.assertEqual(self.database.port, '5000')

    def test_with_wrong_types(self):
        data = DataBaseDTO(None, None, None, None, None)
        with self.assertRaises(TypeError) as context:
            DataBase(data)
        self.assertTrue('None must be a string' in str(context.exception))

    def test_with_wrong_db_name(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.db_name = 'oracle'
        self.assertTrue(f'Unsupported DB: oracle' in str(context.exception))

    def test_with_wrong_user_root(self):
        with self.assertWarns(Warning) as context:
            self.database.user = 'root'
        self.assertTrue('Use root user is dangerous' in str(context.warning))

    def test_with_wrong_password(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.password = 'root1RfG'
        self.assertTrue('Password must be at least' in str(context.exception))

    def test_with_wrong_host(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.host = '10.0.0.777'
        self.assertTrue('\'10.0.0.777\' does not appear' in str(context.exception))

    def test_with_unreachable_host(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.host = '192.168.0.99'
        self.assertTrue('192.168.0.99 is not avaliable' in str(context.exception))

    def test_with_wrong_chars_port(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.port = 'wrong'
        self.assertTrue('Port must contains numbers' in str(context.exception))

    def test_with_min_port(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.port = '0'
        self.assertTrue('Port must be between 0-65000' in str(context.exception))

    def test_with_max_port(self):
        with self.assertRaises(DataBaseException) as context:
            self.database.port = '67000'
        self.assertTrue('Port must be between 0-65000' in str(context.exception))

    def test_with_empty_user(self):
        with self.assertRaises(ValueError) as context:
            data = DataBaseDTO('postgres', '  ', 'qwertyR1!', '127.0.0.1', '5001')
            DataBase(data)
        self.assertTrue('Empty string in values' in str(context.exception))

    def test_database_context(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with DataBase(self.data) as db:
                db.write('Owner', 'Some data')
            self.assertEqual(fake_out.getvalue(), 'Connect to DB: postgres\n'
                                                  'Write Some data to DB: postgres table: Owner\n'
                                                  'Close connect to DB: postgres\n')


if __name__ == '__main__':
    unittest.main()
