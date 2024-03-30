#!/usr/bin/python3

import numpy as np

# Создаем массив
array_to_save = np.array([1, 2, 3, 4, 5])

# Сохраняем массив в файл
np.save('saved_array.npy', array_to_save)

# Загружаем массив из файла
loaded_array = np.load('saved_array.npy')

print(loaded_array)

