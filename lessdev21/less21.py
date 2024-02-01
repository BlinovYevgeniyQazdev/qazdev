import tkinter as tk

# Функция обработки события нажатия кнопки
def on_button_click():
    label.config(text="Кнопка была нажата!")
    # Можно добавить дополнительные действия при нажатии кнопки

# Функция обработки события в текстовом поле
def on_enter(event):
    label.config(text=f"Привет, {entry.get()}!")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Главное окно приложения")

# Метка
label = tk.Label(root, text="Привет, мир!")
label.pack()

# Текстовое поле
entry = tk.Entry(root)
entry.bind("<Return>", on_enter)  # Событие нажатия Enter в текстовом поле
entry.pack()

# Кнопка, которая вызывает функцию on_button_click при нажатии
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()

root.mainloop()
