from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from db_setup import db, Movie, add_new_movie, get_all_movies, update_movie_rate, delete_movie_by_id
from form import MovieForm, UpdateRatingForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"

Bootstrap5(app)
db.init_app(app)

# CREATE DB

with app.app_context():
    db.create_all()

# CREATE TABLE


@app.route("/")
def home():
    list_of_movies = get_all_movies()

    return render_template("index.html", list_movies = list_of_movies)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    
    if form.validate_on_submit():
        new_movie = Movie(
            title = form.title.data,
            year = form.year.data,
            description = form.description.data,
            rating = form.rating.data,
            ranking = form.ranking.data,
            review = form.review.data,
            img_url = form.img_url.data
        )

        add_new_movie(new_movie)

        return redirect('/')
    return render_template('add.html', form=form)

@app.route("/update_movie/<int:id>", methods=['POST', 'GET'])
def update_movie(id):
    form = UpdateRatingForm()
    if form.validate_on_submit():
        rate = form.rating.data
        review = form.review.data 

        update_movie_rate(id, rate, review)

        return redirect('/')
    return render_template('edit.html', form=form)

@app.route("/delete/<int:id>")
def r_delete(id:int):  
    delete_movie_by_id(id)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)
