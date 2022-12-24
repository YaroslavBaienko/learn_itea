import pytest


from database.db import DataBase, DataBaseDTO, DataBaseException


class TestDataBase:
    def setup_method(self):
        self.data = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        self.database = DataBase(self.data)

    def teardown_method(self):
        del self.data
        del self.database

    def test_init_database_correct_data(self):
        assert self.data.db_name == self.database.db_name
        assert self.data.user == self.database.user
        assert self.data.password == self.database.password
        assert self.data.host == self.database.host
        assert self.data.port == self.database.port

    def test_delete_database_instance(self):
        self.database.__del__()
        assert DataBase.instance() is None

    def test_singleton_database_pattern(self):
        data_mysql = DataBaseDTO('mysql', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        data_postgres = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')

        database_mysql = DataBase(data_mysql)
        database_postgres = DataBase(data_postgres)

        assert id(database_mysql) == id(database_postgres)

    def test_connect_to_database(self, capfd):
        self.database.connect()
        assert capfd.readouterr().out == f'Connect to DB: {self.data.db_name}\n'

    def test_close_connect_to_database(self, capfd):
        self.database.close()
        assert capfd.readouterr().out == f'Close connect to DB: {self.database.db_name}\n'

    def test_read_from_database(self, capfd):
        self.database.read('Owner')
        assert f'{self.database.db_name} from table: Owner' in capfd.readouterr().out

    def test_write_to_database(self, capfd):
        self.database.write('Owner', 'Some value')
        assert f'{self.database.db_name} table: Owner' in capfd.readouterr().out

    def test_set_correct_db_name(self):
        self.database.db_name = 'mysql'
        assert self.database.db_name == 'mysql'

    def test_set_correct_user(self):
        self.database.user = 'user'
        assert self.database.user == 'user'

    def test_set_correct_password(self):
        self.database.password = 'user777U!'
        assert self.database.password == 'user777U!'

    def test_set_correct_host(self):
        self.database.host = '8.8.8.8'
        assert self.database.host, '8.8.8.8'

    def test_set_correct_port(self):
        self.database.port = '5000'
        assert self.database.port, '5000'

    def test_with_wrong_types(self):
        data = DataBaseDTO(None, None, None, None, None)
        with pytest.raises(TypeError) as context:
            DataBase(data)
        assert 'None must be a string' in str(context.value)

    def test_with_wrong_db_name(self):
        with pytest.raises(DataBaseException) as context:
            self.database.db_name = 'oracle'
        assert 'Unsupported DB: oracle' in str(context.value)

    def test_with_wrong_user_root(self):
        with pytest.warns(Warning, match=r'Use root user is dangerous'):
            self.database.user = 'root'

    def test_with_wrong_password(self):
        with pytest.raises(DataBaseException) as context:
            self.database.password = 'root1RfG'
        assert 'Password must be at least' in str(context.value)

    def test_with_wrong_host(self):
        with pytest.raises(DataBaseException) as context:
            self.database.host = '10.0.0.777'
        assert '\'10.0.0.777\' does not appear' in str(context.value)

    def test_with_unreachable_host(self):
        with pytest.raises(DataBaseException) as context:
            self.database.host = '192.168.0.99'
        assert '192.168.0.99 is not avaliable' in str(context.value)

    def test_with_wrong_chars_port(self):
        with pytest.raises(DataBaseException) as context:
            self.database.port = 'wrong'
        assert 'Port must contains numbers' in str(context.value)

    def test_with_max_port(self):
        with pytest.raises(DataBaseException) as context:
            self.database.port = '67000'
        assert 'Port must be between 0-65000' in str(context.value)

    def test_empty_with_empty_user(self):
        with pytest.raises(ValueError) as context:
            data = DataBaseDTO('postgres', '  ', 'qwertyR1!', '127.0.0.1', '5001')
            DataBase(data)
        assert 'Empty string in values' in str(context.value)

    def test_database_context(self, capfd):
        with DataBase(self.data) as db:
            db.write('Owner', 'Some data')
        assert capfd.readouterr().out == ('Connect to DB: postgres\n'
                                          'Write Some data to DB: postgres table: Owner\n'
                                          'Close connect to DB: postgres\n')

