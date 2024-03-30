#!/usr/bin/python3


import numpy as np

# Создаем два массива
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2, 4, 6])

# 1. Поэлементное умножение массивов с использованием Broadcasting
product = array1 * array2

# 2. Возведение массива array1 в степень массива array2, с использованием Broadcasting
power = array1 ** array2

# 3. Выполнение операции деления на скаляр каждого массива
scalar_division1 = array1 / 2
scalar_division2 = array2 / 2

# Пример использования Broadcasting с операцией сложения
added_arrays = array1 + array2

# Вывод результатов
print("Поэлементное умножение массивов с использованием Broadcasting:")
print(product)
print("\nВозведение массива array1 в степень массива array2:")
print(power)
print("\nДеление каждого элемента массива array1 на 2:")
print(scalar_division1)
print("\nДеление каждого элемента массива array2 на 2:")
print(scalar_division2)
print("\nСложение массива array2 с каждой строкой массива array1:")
print(added_arrays)

