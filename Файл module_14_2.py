import sqlite3
import random

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# обращаемся к базе при помощи команд
cursor.execute('''  
CREATE TABLE IF NOT EXISTS Users(
Id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
BALANCE INTEGER NOT NULL
)
''')

cursor.execute('DELETE FROM Users WHERE id=?', (6,)) #удалили юзера под номером 6

cursor.execute('SELECT COUNT(*) FROM Users') #считаем количество юзеров, выводим в консоль
total = cursor.fetchone()[0]
print(f'Количество пользователей: {total}')

cursor.execute('SELECT SUM(balance) FROM Users')
SUM_balance = cursor.fetchone()[0]
print(f'Сумма всех балансов равна : {SUM_balance}') # считаем сумму всех балансов

print(f'Средний баланс всех Юзеров : {SUM_balance/ total}')


connection.commit() # сохраняем соединение
connection.close()  # закрываем наше соединение




# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.