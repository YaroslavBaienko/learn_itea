from flask import (
    abort,
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


@weather.route('/', methods=['GET', 'POST'])
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


@weather.route('/show/city')
def show_city():
    """Show cities added into database"""
    cities = City.select()

    country_name = request.args.get('country_name')
    if country_name:
        country = Country.select().where(Country.name == country_name).first()
        if country:
            cities = country.city

    return render_template(
        'weather/show_cities_weather.html',
        title='Show cities weather',
        cities=cities
    )


@weather.route('/show/city/<string:city_name>')
def show_city_detail(city_name):
    """Show detail about city added into database"""
    api_key = current_app.config['WEATHER_API_KEY']
    city_name = city_name.capitalize()

    city = City.select().where(City.name == city_name).first()
    if not city:
        abort(404)

    city_weather = getting_weather(city.name, api_key)
    if 'error' in city_weather:
        flash(city_weather['error'])
        return redirect(url_for('weather.index'))

    city_weather['country'] = city.country.name
    city_weather['name'] = city.name

    return render_template(
        'weather/show_city_detail_weather.html',
        title='Show cities weather',
        city=city_weather
    )


@weather.route('/add/city', methods=['POST'])
def add_city():
    """Add city to monitoring"""
    if request.method == 'POST':
        city = request.form.get('city').capitalize()
        country = request.form.get('country')
        city_check = City.select().where(City.name == city).first()
        if city_check:
            flash(f'{city} already in database')
            return redirect(url_for('weather.index'))

        city_instance = City(
            name=city,
            country=country
        )
        city_instance.save()

        flash(f'City: {city} added to db')

    return redirect(url_for('weather.index'))
