from flask import Flask, jsonify, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random as r

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
with app.app_context():
    db.create_all()

def get_cafe_data():
    response = db.session.execute(db.select(Cafe))
    cafes = response.scalars().all()
    res = r.choice(cafes)

    return res

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    data = get_cafe_data()

    return jsonify(cafe = data.to_dict())

@app.route("/all")
def get_all():
    response = db.session.execute(db.select(Cafe))
    cafe = response.scalars().all()


    data = [item.to_dict() for item in cafe]
    return jsonify(cafe = data)

@app.route("/search")
def search():
    location = request.args.get('loc')
    response = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if len(response) > 0:
        data = [item.to_dict() for item in response]

        return jsonify(cafe = data)
    return jsonify(error = {'not found' : "Sorry we can't find what your looking"})

@app.route("/add", methods =['POST'])
def add_data():
    
    if request.method == "POST":
        new_cafe = Cafe(
            name = request.form.get('name'),
            map_url = request.form.get('map_url'),
            img_url = request.form.get('img_url'),
            location = request.form.get('location'),
            seats= request.form.get('seats'),
            has_toilet = request.form.get('ha_toilet'),
            has_wifi = request.form.get('has_wifi'),
            has_sockets = request.form.get('has_sockets'),
            can_take_calls = request.form.get('can_take_calls'),
            coffee_price = request.form.get('coffee_price')
            )
        
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response = {'success' : 'Succesfully added cafe'})
        

@app.route("/update_price/<int:id>", methods=['PATCH'])
def update_price(id):
    new_price = request.args.get("new_price")

    try:
        cafe = db.get(Cafe, id)
    except AttributeError:
        return jsonify(error = {"Not Found" : "Sorry, a cafe with that id was not found in the database"}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response = {'success' : "Successfully updated the price."}), 200

@app.route("/report_closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api_key")

    if api_key == "TOP_SECRET_KEY":
        try:
            cafe = db.get(Cafe, id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.deleted(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
