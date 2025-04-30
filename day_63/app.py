from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask import Flask
from db_setup import db, Book, update_rating, get_book_by_id, get_all_books, delete_book, add_to_db
from forms import BookForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

Bootstrap5(app)
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = get_all_books()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():

    form = BookForm()

    if form.validate_on_submit():
        print(f'{form.title.data}')

        add_to_db(form.title.data, form.author.data, form.rating.data)
        
        return redirect('/')

    return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=["POST", "GET"])
def edit(id):
    book = get_book_by_id(id)

    if request.method == "POST":
        rating =  request.form['rating']    
        update_rating(id, rating)

        return redirect('/')

    return render_template('edit.html', book = book)

@app.route('/delete/<int:id>', methods=["POST", "GET"])
def delete(id):
    delete_book(id)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
