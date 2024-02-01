import tkinter as tk

def change_label_text():
    label.config(text="Текст изменен")

root = tk.Tk()
root.title("Изменение текста метки")

label = tk.Label(root, text="Нажмите кнопку для изменения этого текста")
label.pack()

change_button = tk.Button(root, text="Изменить текст", command=change_label_text)
change_button.pack()

root.mainloop()
