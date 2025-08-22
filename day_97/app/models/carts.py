from app import db
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,  DeclarativeBase, relationship
from models.users import Users

class Carts(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[str] = mapped_column(String, nullable=False, unique=True)

    items : Mapped[list["CartItem"]] = relationship(
        "CartItem", back_populates="cart", cascade="all, delete-orphan"
    )

    user : Mapped["Users"] = relationship(
        "User", back_populates="carts"
    )

class CartItem(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    cart_id : Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=False)
    product_id : Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    quantity : Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    order : Mapped["Carts"] = relationship("Cart", back_populates="items")
