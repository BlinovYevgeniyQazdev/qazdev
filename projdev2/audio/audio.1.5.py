import tkinter as tk
from tkinter import filedialog, PhotoImage
import pygame
import os
from PIL import Image, ImageTk

class MP3Player:
    def __init__(self, root):
        self.root = root
        root.title('MP3 Player - Green Elephant')
        root.geometry('500x500')
        root.configure(bg='green')

        # Инициализация pygame
        pygame.init()
        pygame.mixer.init()

        # Загрузка изображений
        self.play_image = ImageTk.PhotoImage(Image.open('img/play.jpg').resize((40, 40)))
        self.pause_image = ImageTk.PhotoImage(Image.open('img/pause.jpg').resize((40, 40)))
        self.stop_image = ImageTk.PhotoImage(Image.open('img/stop.jpg').resize((40, 40)))
        self.load_image = ImageTk.PhotoImage(Image.open('img/load.jpg').resize((40, 40)))

        # Создание интерфейса
        self.play_button = tk.Button(root, text='Play.', image=self.play_image, compound='right', command=self.play_music, bg='blue', width=120, height=60)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text='Pause.', image=self.pause_image, compound='right', command=self.pause_music, bg='blue', width=120, height=60)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text='Stop.', image=self.stop_image, compound='right', command=self.stop_music, bg='blue', width=120, height=60)
        self.stop_button.pack(pady=10)

        self.load_button = tk.Button(root, text='Load your mp3 file.', image=self.load_image, compound='right', command=self.load_music, bg='blue', width=200, height=60)
        self.load_button.pack(pady=10)

        # Регулятор громкости
        self.volume_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=self.change_volume, bg='blue', length=200)
        self.volume_scale.set(100)
        self.volume_scale.pack(pady=10)

        self.music_file = None

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.unpause()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def change_volume(self, val):
        volume_level = int(val) / 100
        pygame.mixer.music.set_volume(volume_level)

# Создание окна приложения
root = tk.Tk()
app = MP3Player(root)
root.mainloop()

