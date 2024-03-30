#!/usr/bin/env python3

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблицы, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    user_id INTEGER PRIMARY KEY,
    balance DECIMAL NOT NULL
)
''')

conn.commit()  # Сохранение изменений

# Закрытие соединения
conn.close()
