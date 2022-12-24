from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from peewee import SqliteDatabase

from app.config import config
from app.error_handlers import page_not_found, internal_server_error
from app.base_model import database_proxy
from app.main.models import User
from app.weather.models import Country, City


def create_app(config_name='default'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(config[config_name])

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    db = SqliteDatabase(app.config['DB_NAME'])
    database_proxy.initialize(db)
    db.create_tables([User, Country, City])

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    Bootstrap(app)

    moment = Moment(app)
    moment.init_app(app)

    from app import main
    from app import weather

    app.register_blueprint(main.main)
    app.register_blueprint(weather.weather)

    return app
