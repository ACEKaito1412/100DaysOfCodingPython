import os, requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user




load_dotenv()

CAT_KEY = os.getenv("CAT_KEY")
LINK = 'https://api.thecatapi.com/v1/images/search'

params = {
    'limit' : 12,
    'format' : 'json'
}

headers = {
    'Content-Type' : 'application/json',
    'x-api-key' : CAT_KEY
}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://user.db'
db = SQLAlchemy(model_class=Base)
db.init_app()


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    response = requests.get(url=LINK, params=params, headers=headers)
    data = response.json()
    return render_template('index.html', list_items = data)

@app.route('/like', methods=['POST'])
def liked():
    return

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        new_user = User(
            email = request.form.get("email"),
            password = generate_password_hash(request.form.get("password"), method="pbkdf2", salt_length=8),
            name = request.form.get("name")
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect('/secrets')

    return render_template("register.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            res = db.session.execute(db.select(User).where(User.email == email)).scalar()
            print(res.email)
            if check_password_hash(res.password, password):
                login_user(res)
                return redirect('/secrets')
            else:
                flash("Wrong Password")
                return redirect('/login')
        except AttributeError:
            flash("No user found")
            return redirect('/login')

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)