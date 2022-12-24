import re
import subprocess
import warnings
import ipaddress
from typing import NamedTuple


class DataBaseDTO(NamedTuple):
    db_name: str
    user: str
    password: str
    host: str
    port: str


class DataBaseException(Exception):
    """DataBase base Exception"""


class DataBase:
    __instance = None
    __databases = ('postgres', 'mysql', 'sqlite')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, database: DataBaseDTO):
        self.__check = PersonVerify
        self.__check.verify_all(database, self.databases)

        self.__db_name = database.db_name
        self.__user = database.user
        self.__password = database.password
        self.__host = database.host
        self.__port = database.port

    def __del__(self):
        self.close()
        DataBase.__instance = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        print(f'Connect to DB: {self.db_name}')

    def close(self):
        print(f'Close connect to DB: {self.db_name}')

    def read(self, table: str):
        print(f'Read data from database: {self.db_name} from table: {table}')

    def write(self, table: str, data: str):
        print(f'Write {data} to DB: {self.db_name} table: {table}')

    @property
    def databases(self):
        return self.__databases

    @classmethod
    def instance(cls):
        return cls.__instance

    @property
    def db_name(self):
        return self.__db_name

    @db_name.setter
    def db_name(self, db_name: str):
        self.__check.verify_db_name(db_name, self.databases)
        self.__db_name = db_name

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__check.verify_user(user)
        self.__user = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__check.verify_password(password)
        self.__password = password

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__check.verify_host(host)
        self.__host = host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__check.verify_port(port)
        self.__port = port


class PersonVerify:
    @classmethod
    def verify_all(cls, obj: DataBaseDTO, databases: tuple[str, str, str]):
        cls.verify_db_name(obj.db_name, databases)
        cls.verify_user(obj.user)
        cls.verify_password(obj.password)
        cls.verify_host(obj.host)
        cls.verify_port(obj.port)

    @classmethod
    def verify_type(cls, field: str):
        if not isinstance(field, str):
            raise TypeError(f'{field} must be a string')

    @classmethod
    def verify_empty_field(cls, field: str):
        if not bool(field.strip()):
            raise ValueError('Empty string in values')

    @classmethod
    def verify_db_name(cls, db_name: str, databases: tuple[str, str, str]):
        cls.verify_type(db_name)
        cls.verify_empty_field(db_name)

        if db_name not in databases:
            raise DataBaseException(f'Unsupported DB: {db_name}. Use these names: {databases}')

    @classmethod
    def verify_user(cls, user: str):
        cls.verify_type(user)
        cls.verify_empty_field(user)

        if user == 'root':
            warnings.warn('Use root user is dangerous')

    @classmethod
    def verify_password(cls, password: str):
        cls.verify_type(password)
        cls.verify_empty_field(password)

        length_error = len(password) < 8
        digit_error = re.search(r"\d", password) is None
        uppercase_error = re.search(r"[A-Z]", password) is None
        lowercase_error = re.search(r"[a-z]", password) is None
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

        password_error = any([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

        if password_error:
            raise DataBaseException('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation')

    @classmethod
    def verify_host(cls, host: str):
        cls.verify_type(host)
        cls.verify_empty_field(host)

        try:
            ipaddress.ip_address(host)
        except ValueError as error:
            raise DataBaseException(error)

        with subprocess.Popen(["ping", "-n", "1", host], stdout=subprocess.PIPE) as ping:
            if 'Заданный узел недоступен' in ping.stdout.read().decode('cp866'):
                raise DataBaseException(f'{host} is not avaliable')
            ping.kill()

    @classmethod
    def verify_port(cls, port: str):
        cls.verify_type(port)
        cls.verify_empty_field(port)

        if not port.isnumeric():
            raise DataBaseException(f'Port must contains numbers not {port}')

        if not 0 < int(port) < 65000:
            raise DataBaseException(f'Port must be between 0-65000')


if __name__ == '__main__':
    database_one_dto = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
    database_one = DataBase(database_one_dto)
