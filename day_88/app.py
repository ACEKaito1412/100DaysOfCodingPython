from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from db_setup import db, Cafe, add_new_cafe, remove_cafe, update_cafe, get_all_cafe, get_cafe_by_id
from forms import CafeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"

bootstrap = Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    cafes = get_all_cafe()
    return render_template('index.html', cafes=cafes)

@app.route("/add_cafe", methods=["GET", "POST"])
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
def update_cafe(id):
    cafe = get_cafe_by_id(id)
    form = CafeForm(obj = cafe)
    if form.validate_on_submit():
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
        

        update_cafe(id, name, map_url, img_url, location, coffee_price, has_sockets, has_toilet, has_wifi, can_take_calls, seats)
        return redirect('/')
    return render_template('edit.html', form=form, cafe = cafe)

@app.route("/delete/<int:id>")
def r_delete(id:int):  
    remove_cafe(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)