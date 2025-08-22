from app import db
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.orders import Orders
from models.carts import Carts

class Users(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String, nullable=False)
    email : Mapped[str] = mapped_column(String, nullable=False)
    password : Mapped[str] = mapped_column(String, nullable=False)

    orders : Mapped[list["Orders"]] = relationship(
        "Orders", back_populates="user", cascade="all delete-orphan" 
    )

    cart : Mapped[list["Carts"]] = relationship(
        "Carts", back_populates="user", cascade="all, delete-orphan"
    )