import sqlite3


def initiate_db():
    """Создание таблиц"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );         
    """)
    # ======================================= Изменение функции к новой задаче =======================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,   
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );    
    """)
    # ================================================================================================================
    connection.commit()
    connection.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


# =============================== Добавление новых функций к задаче ==============================================
def add_user(username, email, age, balance=1000):
    """
    Добавляет в таблицу Users запись с переданными данными. Баланс у новых пользователей всегда равен 1000.
    :param username: str, имя пользователя
    :param email: str, почта
    :param age: int, возраст
    :param balance: int, баланс
    """
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES('{username}', '{email}', '{age}', '{balance}')")
    connection.commit()
    connection.close()


def is_included(username):
    """
    Возвращает True, если такой пользователь есть в таблице Users, в противном случае False.
    :param username: str, имя пользователя
    :return: bool, True/False
    """
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
    connection.close()
    if check_user is None:
        return False
    return True


# ================================================================================================================


if __name__ == '__main__':
    # # перед работой бота - инициализация таблицы
    # initiate_db()
    #
    # # перед работой бота заполнение данными БД
    # connection = sqlite3.connect("database.db")
    # cursor = connection.cursor()
    # for i in range(5, 8):
    #     cursor.execute(
    #         f"INSERT INTO Products (id, title, description, price) VALUES('{i}', 'Продукт {i}', 'Описание {i}', '{i * 100}')")
    # connection.commit()
    # connection.close()
    pass
