from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    map_url: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String, nullable=False)
    coffee_price: Mapped[float] = mapped_column(Float, nullable=False)

def add_new_cafe(name:str, map_url:str, img_url:str, location:str, coffee_price:float,
                    has_sockets = False, has_toilet = False, has_wifi = False,
                    can_take_calls = False, seats = False):
    
    new_cafe = Cafe(name = name, map_url = map_url, img_url = img_url,
                    location = location, coffee_price = coffee_price, has_sockets = has_sockets,
                    has_toilet = has_toilet, has_wifi = has_wifi, can_take_calls = can_take_calls,
                    seats = seats)
    
    db.session.add(new_cafe)
    db.session.commit()

def get_all_cafe()->list:
    result = db.session.execute(db.select(Cafe).order_by(Cafe.coffee_price))
    return list(result.scalars())

def get_cafe_by_id(id:int)->Cafe:
    result = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    return result

def update_cafe(id:int, name:str, map_url:str, img_url:str, location:str, coffee_price:float,
                    has_sockets:bool, has_toilet:bool, has_wifi:bool,
                    can_take_calls:bool, seats:bool):
    
    result = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar_one()
    result.name = name
    result.map_url = map_url
    result.img_url = img_url
    result.location = location
    result.coffee_price = coffee_price
    result.has_sockets = has_sockets
    result.has_toilet = has_toilet
    result.has_wifi = has_wifi
    result.can_take_calls = can_take_calls
    result.seats = seats

    db.session.commit()

def remove_cafe(id:int):
    result = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar_one()

    db.session.remove(result)
    db.session.commit()