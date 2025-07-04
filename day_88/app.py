from flask import Flask, render_template, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from db_setup import db, Cafe, User, add_new_cafe, remove_cafe, update_cafe, get_all_cafe, get_cafe_by_id
from forms import CafeForm
from flask_login import login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = "login"

bootstrap = Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/")
def home():
    has_filter = request.args
    has_wifi = request.args.get('wifi') == '1' 
    has_toilet = request.args.get('toilet') == '1' 
    has_socket = request.args.get('socket') == '1' 
    has_calls = request.args.get('can_take_call') == '1' 

    filters = []

    if has_wifi:
        filters.append(Cafe.has_wifi == True)

    if has_toilet:
        filters.append(Cafe.has_toilet == True)
    
    if has_socket:
        filters.append(Cafe.has_sockets == True)

    if has_calls:
        filters.append(Cafe.can_take_calls == True)


    cafes = get_all_cafe(filters=filters, filter_on=has_filter)
    
    return render_template('index.html', cafes=cafes, logged_in = current_user.is_authenticated)

@app.route("/add_cafe", methods=["GET", "POST"])
@login_required
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            location = form.location.data,
            coffee_price = form.coffee_price.data,
            has_sockets = form.has_sockets.data,
            has_toilet = form.has_toilet.data,
            has_wifi = form.has_wifi.data,
            can_take_calls = form.can_take_calls.data,
            seats = form.seats.data,
        )

        add_new_cafe(new_cafe)

        return redirect('/')
    
    return render_template('add.html', form=form)

@app.route("/update_cafe/<int:id>", methods=['POST', 'GET'])
@login_required
def update_cafe_route(id):
    cafe = get_cafe_by_id(id)
    form = CafeForm(obj = cafe)
    form.submit.label.text = "Update Cafe"
    if form.validate_on_submit():
        name = form.name.data
        map_url = form.map_url.data
        img_url = form.img_url.data
        location = form.location.data
        coffee_price = form.coffee_price.data
        has_sockets = form.has_sockets.data
        has_toilet = form.has_toilet.data
        has_wifi = form.has_wifi.data
        can_take_calls = form.can_take_calls.data
        seats = form.seats.data
        
        print(location)

        update_cafe(id=id,name=name, map_url=map_url, img_url=img_url,
                    location = location,coffee_price=coffee_price,has_sockets=has_sockets,
                    has_toilet = has_toilet, has_wifi = has_wifi, can_take_calls = can_take_calls,
                    seats= seats)
        return redirect('/')
    return render_template('edit.html', form=form, cafe = cafe)

@app.route("/delete/<int:id>")
@login_required
def r_delete(id:int):  
    remove_cafe(id)
    return redirect('/')


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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)