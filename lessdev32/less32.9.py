#!/usr/bin/python3



import numpy as np

# Создаем массив из 100 случайных чисел
data = np.random.rand(100)

# Вычисляем среднее значение, медиану и стандартное отклонение
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

print(f"Среднее значение: {mean_value}")
print(f"Медиана: {median_value}")
print(f"Стандартное отклонение: {std_deviation}")
