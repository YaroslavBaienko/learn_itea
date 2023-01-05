import datetime
from peewee import CharField, ForeignKeyField, TextField, DateTimeField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.base_model import BaseModel


class Role(BaseModel):
    name = CharField(max_length=100, unique=True, index=True)


class Profile(BaseModel):
    avatar = CharField()
    info = TextField(null=True)


class User(BaseModel, UserMixin):
    name = CharField(max_length=100)
    email = CharField(max_length=150, unique=True, index=True)
    password_hash = CharField(max_length=128)
    last_visit = DateTimeField(default=datetime.datetime.now)
    role = ForeignKeyField(Role, backref='users')
    profile = ForeignKeyField(Profile)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)



