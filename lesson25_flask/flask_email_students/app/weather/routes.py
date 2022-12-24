from flask import (
    render_template,
    redirect,
    request,
    url_for,
    flash,
    current_app
)

from app.weather import weather
from app.weather.forms import CityForm
from weather.getting_weather import main as getting_weather
from app.weather.models import Country, City


@weather.route('/weather', methods=['GET', 'POST'])
def index():
    """Weather page"""
    form = CityForm()
    city_weather = None
    country = None
    city_name = None

    if form.validate_on_submit():
        api_key = current_app.config['WEATHER_API_KEY']
        city_name = form.city_name.data
        city_weather = getting_weather(city_name, api_key)
        if 'error' in city_weather:
            flash(city_weather['error'])
            return redirect(url_for('weather.index'))
        country = Country.select().where(Country.code == city_weather['country']).first()
        city_weather['country'] = country.name

    return render_template(
        'weather/get_weather.html',
        title='Get city weather',
        form=form,
        city_name=city_name,
        country=country,
        city_weather=city_weather
    )


@weather.route('/weather/add/city', methods=['POST'])
def add_city():
    """Add city to monitoring"""
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')

        city_instance = City(
            name=city,
            country=country
        )
        city_instance.save()
        flash(f'City: {city} added to db')

    return redirect(url_for('weather.index'))
