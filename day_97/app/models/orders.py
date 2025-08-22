from app import db
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,  DeclarativeBase, relationship
from models.users import Users

class Orders(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[str] = mapped_column(String, nullable=False, unique=True)

    items : Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )

    user : Mapped["Users"] = relationship(
        "User", back_populates="orders"
    )

class OrderItem(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id : Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id : Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    quantity : Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    order : Mapped["Orders"] = relationship("Orders", back_populates="items")
