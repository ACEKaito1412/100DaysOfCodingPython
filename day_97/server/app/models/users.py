from app import db
from sqlalchemy import Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum


class RoleEnum(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"


class Users(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)

    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

    orders: Mapped[list["Orders"]] = relationship(
        "Orders", back_populates="user", cascade="all, delete-orphan"
    )

    cart: Mapped["Cart"] = relationship(   # one-to-one
        "Cart", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
