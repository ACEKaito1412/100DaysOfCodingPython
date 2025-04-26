from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(4, 20)])
    submit = SubmitField('Login')