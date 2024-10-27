import sqlite3


def initiate_db():
    """Создание таблицы Products для задания 'Продуктовая база'."""

    connection = sqlite3.connect("database_14_4.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );         
    """)
    connection.commit()
    connection.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""

    connection = sqlite3.connect("database_14_4.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


if __name__ == '__main__':
    # # перед работой бота - инициализация таблицы
    # initiate_db()
    #
    # # перед работой бота заполнение данными БД
    # connection = sqlite3.connect("database_14_4.db")
    # cursor = connection.cursor()
    # for i in range(1, 5):
    #     cursor.execute(
    #         f"INSERT INTO Products (id, title, description, price) VALUES('{i}', 'Продукт {i}', 'Описание {i}', '{i * 100}')")
    # connection.commit()
    # connection.close()
    pass
