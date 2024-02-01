import tkinter as tk
import random

# Функция для проверки угадал ли пользователь число
def guess_number(number):
    if number == secret_number:
        result_label.config(text="Правильно! Вы угадали число!")
    else:
        result_label.config(text=f"Неправильно. Попробуйте еще раз.")

# Генерация секретного числа
secret_number = random.randint(1, 7)

# Создание основного окна
root = tk.Tk()
root.title("Игра 'Угадайка'")
root.geometry("300x200")

# Цвета радуги
rainbow_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']

# Создание фрейма для кнопок
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

# Создание и размещение кнопок
for i, color in enumerate(rainbow_colors, start=1):
    button = tk.Button(buttons_frame, text=str(i), bg=color, command=lambda c=i: guess_number(c))
    button.grid(row=0, column=i)

# Метка для отображения результата
result_label = tk.Label(root, text="Угадайте число от 1 до 7", font=("Helvetica", 16))
result_label.pack(pady=20)

root.mainloop()
