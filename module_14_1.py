import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создаю таблицу Users, если она ещё не создана, с нужными полями
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users
(id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
""")

# Заполняю таблицу Users 10 записями
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000,))

# Обновляю balance у каждой 2ой записи начиная с 1ой на 500
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i,))

# Удаляю каждую 3ую запись в таблице начиная с 1ой
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# Выборка всех записей, где возраст не равен 60 и вывод в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()
