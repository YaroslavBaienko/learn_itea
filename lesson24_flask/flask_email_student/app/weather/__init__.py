from flask import Blueprint

weather = Blueprint('weather', __name__)

from app.weather import routes
