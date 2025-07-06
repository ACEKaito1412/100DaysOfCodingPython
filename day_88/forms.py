from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, FloatField, EmailField, PasswordField
from wtforms.validators import DataRequired

class CafeForm(FlaskForm):
    name            = StringField('Name', validators=[DataRequired()])
    map_url         = StringField("Map Link", validators=[DataRequired()])
    img_url         = StringField("Img Link", validators=[DataRequired()])
    location        = StringField("Map", validators=[DataRequired()])
    has_sockets     = BooleanField("Has Sockets")
    has_toilet      = BooleanField("Has Toilet")
    has_wifi        = BooleanField("Has Wifi")
    can_take_calls  = BooleanField("Can Take Calls")
    seats           = StringField("How many seats", validators=[DataRequired()])
    coffee_price    = StringField("Coffee Price", validators=[DataRequired()])
    submit          = SubmitField("Add Cafe")



class RegisterForm(FlaskForm):
    name        = StringField('Name', validators=[DataRequired()])
    email       = EmailField('Email Address', validators=[DataRequired()])
    pasword     = PasswordField('Password', validators=[DataRequired()])
    sign_up     = SubmitField('Sign-Up')

class LoginForm(FlaskForm):
    email       = EmailField('Email Address', validators=[DataRequired()])
    pasword     = PasswordField('Password', validators=[DataRequired()])
    login       = SubmitField('Log-in')