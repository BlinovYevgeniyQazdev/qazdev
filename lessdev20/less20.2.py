import tkinter as tk

def clear_text():
    entry.delete(0, tk.END)

def on_enter(event):
    clear_text()

root = tk.Tk()
root.title("Текстовое поле и кнопка 'Очистить'")

entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", on_enter)

clear_button = tk.Button(root, text="Очистить", command=clear_text)
clear_button.pack()

root.mainloop()
