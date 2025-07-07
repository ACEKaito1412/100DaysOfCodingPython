from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



class Todo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('user.id') ,nullable=False)
    task: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now())
    deadline_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    user = relationship("User", back_populates="todos")

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    todos = relationship("Todo", back_populates="user", cascade="all, delete-orphan")


def add_new_user(user:User):
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email:str)->User:
    res = db.session.execute(db.select(User).where(User.email == email)).scalar_one()
    return res

def add_new_todo(todo:Todo):
    db.session.add(todo)
    db.session.commit()

def update_todo(id:int, todo:Todo):
    res = db.session.execute(db.select(Todo).where(Todo.id == id)).scalar_one()
    if res:
        res.task = todo.task
        res.status = todo.status
        res.deadline_date = todo.deadline_date

    db.session.commit()

def get_user_todos(user_id:int)->list:
    res = db.session.execute(db.select(Todo).where(Todo.user_id == user_id))
    return list(res.scalars())


