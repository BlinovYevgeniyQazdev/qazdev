#!/usr/bin/python3

import numpy as np

# Генерация массива случайных чисел
random_array = np.random.rand(10)

# Вычисление среднего, медианы и стандартного отклонения
mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_deviation = np.std(random_array)

print("Среднее:", mean_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)

