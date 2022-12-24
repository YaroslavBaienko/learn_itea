from peewee import CharField, ForeignKeyField

from app.base_model import BaseModel


class Country(BaseModel):
    code = CharField(max_length=2, unique=True, index=True)
    name = CharField(max_length=100, unique=True, index=True)


class City(BaseModel):
    name = CharField(max_length=100, unique=True, index=True)
    country = ForeignKeyField(Country, backref='city')
