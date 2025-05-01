from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=base)

class Movie(db.Model):
    id : Mapped[Integer] = mapped_column(Integer, primary_key=True)
    title : Mapped[String] = mapped_column(String, nullable=False, unique=True)  
    year : Mapped[Integer] = mapped_column(Integer, nullable=False)
    description : Mapped[String] = mapped_column(String, nullable=False)
    rating : Mapped[Float] = mapped_column(Float, nullable=False)
    ranking : Mapped[Integer] = mapped_column(Integer, nullable=False)
    review : Mapped[String] = mapped_column(String, nullable=False)
    img_url : Mapped[String] = mapped_column(String, nullable=False)


def add_new_movie(movie:Movie):
    db.session.add(movie)
    db.session.commit()

def get_all_movies()->list:
    res = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    return list(res)

def update_movie_rate(id:int, rating:float, review:str):
    res = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    res.rating = rating
    res.review = review
    db.session.commit()

def delete_movie_by_id(id:int):
    res = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()

    db.session.delete(res)
    db.session.commit()
