from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CityForm(FlaskForm):
    city_name = StringField(
        'What city weather are you interested in?',
        validators=[DataRequired(), Length(3, 100)],
        render_kw={'placeholder': 'Full name'}
    )
    submit = SubmitField('Show')
