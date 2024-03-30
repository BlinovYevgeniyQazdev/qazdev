#!/usr/bin/python3

import numpy as np

# Создание массива для примера
data = np.array([10, 15, 12, 8, 14, 20, 18, 16, 17, 11])

# Сумма элементов массива
total = np.sum(data)

# Среднее значение
mean_value = np.mean(data)

# Медиана
median_value = np.median(data)

# Минимальное и максимальное значения
min_value = np.min(data)
max_value = np.max(data)

# Стандартное отклонение и дисперсия
std_deviation = np.std(data)
variance = np.var(data)

print("Сумма:", total)
print("Среднее значение:", mean_value)
print("Медиана:", median_value)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Стандартное отклонение:", std_deviation)
print("Дисперсия:", variance)
