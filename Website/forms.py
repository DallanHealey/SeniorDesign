from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UserSettings(FlaskForm):
    email = StringField('Email')
    phone = StringField('Phone Number')
    submit = SubmitField('Save')