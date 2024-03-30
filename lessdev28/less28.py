#!/usr/bin/env python3
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

try:
    # Начало транзакции
    conn.execute('BEGIN TRANSACTION')
    
    # Внесение изменений в базу данных
    cursor.execute('UPDATE accounts SET balance = balance - 100 WHERE user_id = 1')
    cursor.execute('UPDATE accounts SET balance = balance + 100 WHERE user_id = 2')
    
    # Симуляция ошибки
    raise Exception('Simulated error')
    
except Exception as e:
    # Откат изменений при возникновении ошибки
    conn.execute('ROLLBACK')
    print(f'Error: {e}')
    
finally:
    # Закрытие соединения
    conn.close()

