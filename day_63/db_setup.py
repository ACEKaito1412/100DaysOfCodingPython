from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[int] = mapped_column(Float, nullable=False)

def add_to_db(title:str, author:str, rating:int):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

def get_all_books()->list:
    result = db.session.execute(db.select(Book).order_by(Book.title))
    return list(result.scalars())
    
def get_book_by_id(id:int)->Book:
    result = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    return result

def update_rating(id:int, rating:int):
    res = db.session.execute(db.select(Book).where(Book.id == id)).scalar_one()
    res.rating = rating
    db.session.commit()

def delete_book(id:int):
    res = db.session.execute(db.select(Book).where(Book.id == id)).scalar_one()
    db.session.delete(res)
    db.session.commit()
