import sqlite3

# Функция для инициализации базы данных и таблиц
def initialize_db(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            status TEXT,
            country TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            stock INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            balance REAL,
            status TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            salary REAL
        );
    ''')
    conn.commit()

# Функция для выполнения SQL-запросов по задачам
def execute_task(cursor, task_number):
    if task_number == 1:
        cursor.execute('SELECT * FROM orders')
        for row in cursor.fetchall():
            print(row)
    
    elif task_number == 2:
        cursor.execute('SELECT DISTINCT category FROM products')
        for row in cursor.fetchall():
            print(row)
    
    elif task_number == 3:
        balance_threshold = float(input("Введите порог баланса для поиска клиентов: "))
        cursor.execute('SELECT first_name, last_name FROM customers WHERE balance > ?', (balance_threshold,))
        for row in cursor.fetchall():
            print(row)
    
    elif task_number == 4:
        cursor.execute('SELECT * FROM employees ORDER BY salary DESC')
        for row in cursor.fetchall():
            print(row)

    elif task_number == 5:
        cursor.execute('UPDATE employees SET salary = salary * 1.05')
        print("Зарплаты сотрудников увеличены на 5%.")
    
    elif task_number == 6:
        cursor.execute("UPDATE orders SET status = 'Processing' WHERE country = 'USA'")
        print("Статус заказов обновлен на 'Processing' для страны 'USA'.")
    
    elif task_number == 7:
        cursor.execute('UPDATE products SET price = price * 0.9 WHERE stock < 20')
        print("Цены на продукты с запасом меньше 20 уменьшены на 10%.")
    
    elif task_number == 8:
        cursor.execute("UPDATE customers SET status = 'Active' WHERE balance > 5000")
        print("Статус клиентов с балансом выше 5000 изменен на 'Active'.")

# Основной цикл приложения

def main():
    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        initialize_db(conn, cursor)




        
        while True:
            print("\nДоступные задачи:")
            print("1. Показать все заказы")
            print("2. Показать уникальные категории продуктов")
            print("3. Показать клиентов с балансом выше заданного значения")
            print("4. Показать сотрудников, отсортированных по зарплате")
            print("5. Увеличить зарплату сотрудников на 5%")
            print("6. Обновить статус заказов 'Processing' для USA")
            print("7. Уменьшить цену продуктов с низким запасом на 10%")
            print("8. Изменить статус клиентов на 'Active' при балансе выше 5000")
            print("0. Выйти из программы")
            task_number = int(input("Выберите номер задачи для выполнения: "))
            
            if task_number == 0:
                break
            elif 1 <= task_number <= 8:
                execute_task(cursor, task_number)
            else:
                print("Неверный выбор. Пожалуйста, введите номер от 0 до 8.")
            
            conn.commit()

if __name__ == "__main__":
    main()
