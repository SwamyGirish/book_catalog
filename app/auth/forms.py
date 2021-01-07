from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email

class RegistrationForm(FlaskForm):
    name = StringField('Enter your name: ')
    email = StringField('Enter your email: ')
    submit = SubmitField('Register')