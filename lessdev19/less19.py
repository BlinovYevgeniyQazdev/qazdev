import tkinter as tk

# Задача 1: Создание простого окна с кнопкой "Выход"
def create_exit_window():
    window = tk.Tk()
    window.title("Закрытие окна")
    exit_button = tk.Button(window, text="Выход", command=window.destroy)
    exit_button.pack(pady=20)
    window.mainloop()

# Задача 2: Создание окна с анкетой
def create_info_window():
    info_window = tk.Tk()
    info_window.title("Анкета")
    label = tk.Label(info_window, text="Здесь может быть ваша анкета")
    label.pack(pady=20)
    info_window.mainloop()

# Вызов функции для создания окна с кнопкой "Выход"
create_exit_window()

# Вызов функции для создания окна с анкетой (раскомментируйте следующую строку, чтобы запустить)
create_info_window()
