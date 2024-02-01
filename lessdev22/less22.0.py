import tkinter as tk

# Функция для обновления текстовой области содержимым текстового поля
def update_text_area():
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

# Функция для очистки текстовой области
def clear_text_area():
    text_area.delete('1.0', tk.END)

root = tk.Tk()
root.title("Интерфейс с метками, кнопками и текстовым полем")

# Создание меток
label1 = tk.Label(root, text="Введите текст:")
label1.pack()
label2 = tk.Label(root, text="Ваш текст ниже:")
label2.pack()

# Создание текстового поля
entry = tk.Entry(root, width=50)
entry.pack()

# Создание кнопок с привязанными функциями
update_button = tk.Button(root, text="Обновить текстовую область", command=update_text_area)
update_button.pack()
clear_button = tk.Button(root, text="Очистить текстовую область", command=clear_text_area)
clear_button.pack()

# Создание текстовой области
text_area = tk.Text(root, height=10, width=50)
text_area.pack()

root.mainloop()
