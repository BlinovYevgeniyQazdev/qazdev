import tkinter as tk
from tkinter import PhotoImage
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Определение базового класса моделей
Base = declarative_base()

# Определение модели Person
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Создание движка SQLAlchemy и сессии
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Функция для вставки нового Person в базу данных
def insert_person():
    try:
        # Перед созданием объекта Person необходимо убедиться, что поля заполнены корректно.
        # Если поля пустые или содержат некорректные данные, должно быть выброшено исключение.
        new_id = int(id_entry.get())
        new_name = name_entry.get()
        new_age = int(age_entry.get())

        if not new_name:
            raise ValueError("Имя не может быть пустым.")

        new_person = Person(id=new_id, name=new_name, age=new_age)
        session.add(new_person)
        session.commit()
        result_label.config(text=f"Добавлен новый человек: ID {new_person.id}, Имя {new_person.name}, Возраст {new_person.age}")
    except Exception as e:
        session.rollback()  # В случае ошибки откатывает незавершенные транзакции
        result_label.config(text=f"Ошибка: {e}")



# Создание основного окна Tkinter
root = tk.Tk()
root.title("Добавление данных в базу")

# Поля для ввода id, name и age
tk.Label(root, text="ID").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Age").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

# Загрузка изображения
image_path = 'f04.png'  # Убедитесь, что файл находится в той же директории, что и скрипт
button_image = PhotoImage(file=image_path)

# Кнопка с изображением
insert_button = tk.Button(root, image=button_image, command=insert_person)
insert_button.grid(row=3, column=0, columnspan=2)

# Чтобы изображение не исчезло из-за сборщика мусора Python, свяжите его с виджетом
insert_button.image = button_image


# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Запуск главного цикла Tkinter
root.mainloop()
