import sqlite3

# Функция для добавления данных сотрудника
def add_employee(conn):
    id = input("Введите ID сотрудника: ")
    name = input("Введите имя сотрудника: ")
    position = input("Введите должность сотрудника: ")
    salary = input("Введите зарплату сотрудника: ")

    try:
        with conn:
            conn.execute('''
                INSERT INTO Employees (id, name, position, salary)
                VALUES (?, ?, ?, ?);
            ''', (id, name, position, salary))
        print("Данные сотрудника добавлены успешно.")
    except sqlite3.IntegrityError:
        print("Ошибка: ID сотрудника уже существует.")
    except sqlite3.Error as e:
        print("Ошибка при добавлении данных сотрудника:", e)

# Функция для отображения существующих данных сотрудников
def view_employees(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees;')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Функция для редактирования данных сотрудника
def edit_employee(conn):
    id = input("Введите ID сотрудника для редактирования: ")
    new_name = input("Введите новое имя сотрудника: ")
    new_position = input("Введите новую должность сотрудника: ")
    new_salary = input("Введите новую зарплату сотрудника: ")

    try:
        with conn:
            conn.execute('''
                UPDATE Employees
                SET name = ?, position = ?, salary = ?
                WHERE id = ?;
            ''', (new_name, new_position, new_salary, id))
        print("Данные сотрудника обновлены успешно.")
    except sqlite3.Error as e:
        print("Ошибка при редактировании данных сотрудника:", e)

# Основная программа
def main():
    # Подключаемся к базе данных
    conn = sqlite3.connect('mydatabase.db')

    while True:
        print("\nВыберите действие:")
        print("1. Добавить сотрудника")
        print("2. Посмотреть текущих сотрудников")
        print("3. Выйти")
        print("4. Изменить данные сотрудника")
        choice = input("Ввод: ")

        if choice == "1":
            add_employee(conn)
        elif choice == "2":
            view_employees(conn)
        elif choice == "3":
            break
        elif choice == "4":
            edit_employee(conn)
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2, 3 или 4.")

    # Закрываем соединение с базой данных
    conn.close()

if __name__ == "__main__":
    main()
