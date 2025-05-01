from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    year = StringField('Author', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = IntegerField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image Url', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateRatingForm(FlaskForm):
    rating = StringField('Your rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')