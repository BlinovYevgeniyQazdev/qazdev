import sqlite3
import csv
import os

# Определяем путь к директории, где находится этот скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'outputfile.csv')

# Создаем соединение с базой данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

try:
    # Проверяем, существует ли таблица Employees, и если нет, создаем ее
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Employees';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE Employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL
            );
        ''')
        conn.commit()
        print("Таблица 'Employees' создана, так как не существовала.")

    # Теперь, когда у нас есть таблица Employees, мы можем выполнить наш запрос
    cursor.execute('SELECT * FROM Employees;')

    # Получаем результаты
    results = cursor.fetchall()

    # Проверяем, есть ли записи в таблице, прежде чем пытаться записать их в CSV
    if results:
        # Записываем результаты в файл CSV
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Записываем заголовки столбцов в CSV
            csvwriter.writerow([desc[0] for desc in cursor.description])
            # Записываем все строки из таблицы Employees в CSV
            csvwriter.writerows(results)
        print("Данные записаны в файл:", csv_file_path)
    else:
        print("В таблице 'Employees' нет данных для записи.")

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # Закрываем соединение с базой данных
    conn.close()
