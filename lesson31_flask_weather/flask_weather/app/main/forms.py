from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length


class GenerateDataForm(FlaskForm):
    submit = SubmitField('Generate')


class NameForm(FlaskForm):
    id = HiddenField('id')
    name = StringField(
        'What is your name?',
        validators=[DataRequired(), Length(3, 100)],
        render_kw={'placeholder': 'Full name'}
    )
    email = EmailField(
        'What is your email?',
        validators=[DataRequired(), Length(10, 150)],
        render_kw={'placeholder': 'Email'}
    )
    submit = SubmitField('Add')
