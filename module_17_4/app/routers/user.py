from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """
    Возвращает список всех пользователей из БД
    :param db: БД
    :return: Список всех пользователей из БД
    """
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
    Получение записи о пользователе по id
    :param db: БД
    :param user_id: id пользователя
    :return: Запись из БД о пользователе
    """
    user = db.scalars(select(User).where(User.id == user_id))  # получение записи о пользователе
    if user is None:  # если пользователя с таким user_id не существует
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    return user


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], new_user: CreateUser):
    """
    Создание новой записи о новом пользователе
    :param db: БД
    :param new_user: данные о новом пользователе согласно полям schemas.CreateUser
    :return: Словарь с сообщением об удачном/неудачном добавлении пользователя
    """
    # проверка на существование пользователя с входящими данными по полям [username, firstname, lastname]
    old_user = db.scalars(select(User).where(
        User.username == new_user.username and User.firstname == new_user.firstname and User.lastname == new_user.lastname))
    if old_user is None:  # если пользователя такого нет, то создаем новую запись с новым пользователем
        db.execute(insert(User).values(
            username=new_user.username,
            firstname=new_user.firstname,
            lastname=new_user.lastname,
            age=new_user.age,
            slug=slugify(new_user.username)
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    else:  # Ответ в случае попытки создания дубликата пользователя
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Such a user already exists"
        )


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user: UpdateUser, user_id: int):
    """
    Изменение записи о пользователе
    :param db: БД
    :param user: изменяемые данные о пользователе согласно полям schemas.UpdateUser
    :param user_id: id пользователя
    :return: Словарь об успешном изменении записи / Исключение, если запись о пользователе не найдена
    """
    old_user = db.scalars(select(User).where(User.id == user_id))  # получение записи нужного пользователя
    if old_user is None:  # если пользователь не найден, то генерирую исключение
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    # изменяю запись пользователя в БД
    db.execute(update(User).where(User.id == user_id).values(
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
    Удаление записи о пользователе
    :param db: БД
    :param user_id: id пользователя
    :return: Словарь об успешном удалении записи / Исключение, если запись о пользователе не найдена
    """
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
