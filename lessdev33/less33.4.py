#!/usr/bin/python3

import numpy as np

# Создаем одномерный массив
original_array = np.array([5, 2, 8, 9, 1])

# Изменяем форму массива
reshaped_array = original_array.reshape((5, 1))

# Сортируем массив
sorted_array = np.sort(reshaped_array, axis=0)

print(sorted_array)

