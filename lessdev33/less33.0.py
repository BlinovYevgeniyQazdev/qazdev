#!/usr/bin/python3


import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

# Доступ к элементу по индексу
print(arr_1d[2])  # Вывод: 3

# Массив с индексами
indices = np.array([1, 3])
print(arr_1d[indices])  # Вывод: [2, 4]

