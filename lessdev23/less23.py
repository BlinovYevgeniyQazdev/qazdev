import tkinter as tk
from tkinter import ttk

# Функция вызывается при выборе элемента в выпадающем списке
def on_combobox_select(event):
    selected_item = combobox.get()
    selection_label.config(text=f"Вы выбрали: {selected_item}")

root = tk.Tk()
root.title("Интерфейс с выпадающим списком")

# Создание фрейма для выпадающего списка
combobox_frame = tk.Frame(root)
combobox_frame.pack(pady=10)

# Создание и размещение метки для выпадающего списка
combobox_label = tk.Label(combobox_frame, text="Выберите элемент:")
combobox_label.pack(side=tk.LEFT)

# Создание списка элементов
items = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4"]

# Создание и размещение выпадающего списка
combobox = ttk.Combobox(combobox_frame, values=items)
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox.pack(side=tk.LEFT)

# Создание фрейма для отображения выбранного элемента
selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

# Создание и размещение метки для отображения выбранного элемента
selection_label = tk.Label(selection_frame, text="Здесь будет отображаться ваш выбор")
selection_label.pack()

root.mainloop()
