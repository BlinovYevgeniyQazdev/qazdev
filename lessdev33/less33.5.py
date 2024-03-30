#!/usr/bin/python3


import numpy as np

# Создаем одномерный массив
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Создаем булеву маску для фильтрации
mask = (data > 5) & (data < 10)

# Применяем маску
filtered_data = data[mask]

print(filtered_data)

