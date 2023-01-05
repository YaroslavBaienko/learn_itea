from peewee import SqliteDatabase

from app.base_model import database_proxy
from app.weather.models import Country


db = SqliteDatabase('user.db')
database_proxy.initialize(db)
db.create_tables([Country])


# import hashlib
#
# email = "someone111@somewhere.com"
# size = 80
#
# digest = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
# url = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
#             digest, size)
