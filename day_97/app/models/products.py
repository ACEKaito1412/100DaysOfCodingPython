from app import db
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String, nullable=False)
    price : Mapped[float] = mapped_column(Float, nullable=False)
    stock : Mapped[int] = mapped_column(Integer, nullable=False)
  