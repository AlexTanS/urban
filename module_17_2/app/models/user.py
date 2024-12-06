from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column
from module_17_2.app.backend import db


class User(db.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # целое число, первичный ключ, с индексом
    username = Column(String)  # строка
    firstname = Column(String)  # строка
    lastname = Column(String)  # строка
    age = Column(Integer)  # целое число
    slug = Column(String, unique=True, index=True)  # строка, уникальная, с индексом

    tasks = relationship("Task",
                         back_populates="user")  # объект связи с таблицей с таблицей Task, где back_populates='user'
