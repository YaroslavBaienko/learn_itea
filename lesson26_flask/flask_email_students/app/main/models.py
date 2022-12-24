from peewee import CharField

from app.base_model import BaseModel


class User(BaseModel):
    name = CharField(max_length=100)
    email = CharField(max_length=150, unique=True, index=True)
    phone = CharField(max_length=100, null=True)
