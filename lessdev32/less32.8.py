#!/usr/bin/python3


import numpy as np

def sum_rows(arr):
    rows_sums = np.sum(arr, axis=1)
    return rows_sums

arr1 = np.random.randint(1, 10, size=(3,3))
arr2 = np.random.randint(1, 10, size=(3,3))

result = np.multiply(arr1, arr2)

print(f"Array1:{arr1}")
print(f"Array2:{arr2}")

sums_row1 = sum_rows(arr1)
sums_row2 = sum_rows(arr2)

# print(f"\n result {result}")

print(f"Summa1{sums_row1}")
print(f"Summa2{sums_row2}")
