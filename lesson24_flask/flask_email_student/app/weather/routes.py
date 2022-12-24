from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    current_app
)

from app.weather import weather
from app.weather.forms import CityForm


@weather.route('/weather', methods=['GET', 'POST'])
def index():
    """Weather page"""
    form = CityForm()

    if form.validate_on_submit():
        print(form.city_name.data)

    return render_template(
        'weather/get_weather.html',
        title='Get city weather',
        form=form
    )
