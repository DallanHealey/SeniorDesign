from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class UserSettings(FlaskForm):
    email = StringField('Email')
    phone = StringField('Phone Number')
    sendEmail = BooleanField("Send Email?")

    submit = SubmitField('Save')