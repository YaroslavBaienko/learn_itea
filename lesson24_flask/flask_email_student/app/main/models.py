from peewee import *


database_proxy = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


class User(BaseModel):
    name = CharField(max_length=100)
    email = CharField(max_length=150, unique=True, index=True)
