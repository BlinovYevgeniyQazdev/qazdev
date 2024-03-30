#!/usr/bin/python3


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

# Сравнение поэлементно
equal_arr = arr1 == arr2
greater_arr = arr1 > arr2

print("Равенство:", equal_arr)
print("Больше:", greater_arr)
