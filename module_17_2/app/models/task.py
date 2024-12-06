from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, String, Boolean, Column
from module_17_2.app.backend import db


class Task(db.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # целое число, первичный ключ, с индексом
    title = Column(String)  # строка
    content = Column(String)  # строка
    priority = Column(Integer, default=0)  # целое число, по умолчанию 0
    completed = Column(Boolean, default=False)  # булево значение, по умолчанию False
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False,
                     index=True)  # целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом
    slug = Column(String, unique=True, index=True)  # строка, уникальная, с индексом

    user = relationship("User",
                        back_populates="tasks")  # объект связи с таблицей с таблицей User, где back_populates='tasks'
