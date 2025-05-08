from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))



with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)


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


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name = name, logged_in = current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
def download():
    return send_from_directory('static/files/', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
