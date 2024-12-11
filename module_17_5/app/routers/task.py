from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic
from typing import Annotated
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask
# Функции работы с записями
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    """
    Возвращает список все записи о задачах из БД
    :param db: БД
    :return: Список всех записей задач из БД
    """
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    """
    Получение записи о задаче по id
    :param db: БД
    :param task_id: id задачи
    :return: Запись из БД о задаче
    """
    task = db.scalar(select(Task).where(Task.id == task_id))  # получение записи о задаче
    if task is None:  # если пользователя с таким user_id не существует
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    return task


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], new_task: CreateTask, user_id: int):
    """
    Создание новой записи о задаче
    :param db: БД
    :param new_task: данные о новой задаче согласно полям schemas.CreateTask
    :param user_id: id пользователя с которым надо связать задачу
    :return: Словарь с сообщением об удачном/неудачном добавлении записи о задаче
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:  # если пользователя такого нет, то выкидываю исключение
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    else:  # если пользователь с таким id существует, то создаю запись о задаче в БД
        db.execute(insert(Task).values(
            title=new_task.title,
            content=new_task.content,
            priority=new_task.priority,
            user_id=user_id,
            slug=slugify(new_task.title)
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task: UpdateTask, task_id: int):
    """
    Изменение записи о задаче
    :param db: БД
    :param task: изменяемые данные о задаче согласно полям schemas.UpdateTask
    :param task_id: id задачи
    :return: Словарь об успешном изменении записи / Исключение, если запись о задаче не найдена
    """
    old_task = db.scalar(select(Task).where(Task.id == task_id))
    if old_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=task.title,
        content=task.content,
        priority=task.priority,
        slug=slugify(task.title)
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    """
    Удаление записи о задаче
    :param db: БД
    :param task_id: id задачи
    :return: Словарь об успешном удалении записи / Исключение, если запись о пользователе не найдена
    """
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
















