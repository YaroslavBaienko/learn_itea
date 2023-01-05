from flask import (
    abort,
    render_template,
    redirect,
    request,
    url_for,
    flash,
    current_app
)
from flask_login import login_required, current_user

from app.weather import weather
from app.weather.forms import CityForm
from weather.getting_weather import main as getting_weather
from app.weather.models import Country, City, User, UserCity


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
@login_required
def show_city():
    """Show cities added into database"""
    user_cities = (
        UserCity
        .select(City)
        .join(User)
        .switch(UserCity)
        .join(City)
        .where(UserCity.user == current_user.id)
    )

    country_name = request.args.get('country_name')
    if country_name:
        user_cities = [city for city in user_cities if city.city.country.name == country_name]

    return render_template(
        'weather/show_cities_weather.html',
        title='Show cities weather',
        cities=user_cities
    )


@weather.route('/show/city/<string:city_name>')
@login_required
def show_city_detail(city_name):
    """Show detail about city added into database"""
    api_key = current_app.config['WEATHER_API_KEY']
    city_name = city_name.capitalize()

    user_city = (
        UserCity
        .select(City)
        .join(User)
        .where(User.id == current_user.id)
        .switch(UserCity)
        .join(City)
        .where(City.name == city_name).first()
    )

    if not user_city:
        abort(404)

    city_weather = getting_weather(user_city.city.name, api_key)
    if 'error' in city_weather:
        flash(city_weather['error'])
        return redirect(url_for('weather.index'))

    city_weather['country'] = user_city.city.country.name
    city_weather['name'] = user_city.city.name
    city_weather['flag_url'] = user_city.city.country.flag
    return render_template(
        'weather/show_city_detail_weather.html',
        title='Show cities weather',
        city=city_weather
    )


@weather.route('/add/city', methods=['GET', 'POST'])
@login_required
def add_city():
    """Add city to monitoring"""
    if request.method == 'POST':
        city = request.form.get('city').capitalize()

        city_instance = City.select().where(City.name == city).first()
        if not city_instance:
            country = request.form.get('country')
            city_instance = City(
                name=city,
                country=country
            )
            city_instance.save()

        user_city = UserCity.select().where(UserCity.user == current_user, UserCity.city == city_instance).first()
        if user_city:
            flash(f'City {city} already in list of user {current_user.name}')
            return redirect(url_for('main.index'))

        user_city = UserCity(user=current_user, city=city_instance)
        user_city.save()

        flash(f'City: {city} added to list of user {current_user.name}')

    return redirect(url_for('weather.index'))


@weather.route('/delete/city', methods=['POST'])
@login_required
def delete_cities():
    """Delete selected cities for current user"""
    if request.method == 'POST':
        message = 'Deleted: '
        selectors = list(map(int, request.form.getlist('selectors')))

        if not selectors:
            flash('Nothing to delete')
            return redirect(url_for('weather.show_city'))

        (
            UserCity
            .delete()
            .where(UserCity.user == current_user.id, UserCity.city.in_(selectors)).execute()
        )

        cities_to_delete = City.select().where(City.id.in_(selectors))
        for city in cities_to_delete:
            message += f'{city.name}, '
        flash(message[:-2])
        return redirect(url_for('weather.show_city'))
