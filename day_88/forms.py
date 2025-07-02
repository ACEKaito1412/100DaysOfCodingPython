from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired

class CafeForm(FlaskForm):
    name            = StringField('Name', validators=[DataRequired()])
    map_url         = StringField("Map Link", validators=[DataRequired()])
    img_url         = StringField("Img Link", validators=[DataRequired()])
    location        = StringField("Map", validators=[DataRequired()])
    has_sockets     = BooleanField("Has Sockets", validators=[DataRequired()])
    has_toilet      = BooleanField("Has Toilet", validators=[DataRequired()])
    has_wifi        = BooleanField("Has Wifi", validators=[DataRequired()])
    can_take_calls  = BooleanField("Can Take Calls", validators=[DataRequired()])
    seats           = BooleanField("Has Sockets", validators=[DataRequired()])
    coffee_price    = FloatField("Coffee Price", validators=[DataRequired()])
    submit          = SubmitField("Add Cafe")
