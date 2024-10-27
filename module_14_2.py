import sqlite3

connection = sqlite3.connect("not_telegram_14_2.db")
cursor = connection.cursor()

# =========================== Код от предыдущей задачи ===========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users
(id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
""")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000,))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i,))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")
# ================================================================================

# Удаляю из базы данных запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
total = cursor.fetchone()[0]

# Вывод в консоль среднего баланса всех пользователей
# 1 вариант
print(total / count)
# 2 вариант
cursor.execute("SELECT AVG(balance) FROM Users")
print(cursor.fetchone()[0])

connection.commit()
connection.close()
