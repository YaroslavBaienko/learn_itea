class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.close()
        DataBase.__instance = None

    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        print(f'Connect to DB: {self.db_name}')

    def close(self):
        print(f'Close connect to DB: {self.db_name}')

    def read(self, table):
        print(f'Read data from database: {self.db_name} from table: {table}')

    def write(self, table, data):
        print(f'Write {data} to DB: {self.db_name} table: {table}')


database = DataBase('postgres', 'root', 'qwerty', 'localhost', '5001')
database.connect()
database.write('persons', 'Some data')
print(id(database))

database_new = DataBase('mysql', 'root', 'qwerty', 'localhost', '2077')
database_new.connect()
print(id(database_new))
