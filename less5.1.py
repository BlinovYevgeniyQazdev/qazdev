#!/usr/bin/python3.11

# Example number 1
print("ПРИМЕР НОМЕР 1")
print("======================================================================================")
for i in range(0, 21, 2): #разбор того что написано в скобках первое это откуда мы начинаем, второе до какого числа идём, треть с каким шагом
    print(i)
print("======================================================================================")

# Example number 2
print("ПРИМЕР НОМЕР 2 Таблица умножения до 10")
print("======================================================================================")
#Запрос числа у пользователя
num = int(input("Введите число: "))
#Вывод таблицы умножения
print(f"Таблица умножения для числа {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
print("======================================================================================")

# Example number 3
print("ПРИМЕР НОМЕР 3 Таблица умножения до 5")
print("======================================================================================")
num = int(input("Введите число: "))
#Вывод таблицы умножения
print(f"Таблица умножения для числа {num}:")
for i in range(1, 5):
    result = num * i
    print(f"{num} x {i} = {result}")
print("======================================================================================")


# Example number 4
print("ПРИМЕР НОМЕР 4 Таблица умножения до 5 c ВЛОЖЕННЫМИ ЦИКЛАМИ")
print("======================================================================================")
for i in range(1,2):
    for j in range(1, 6):
        tab = i * j
        print(f"{i} X {j} = {tab}")
    print()
print("======================================================================================")

# Example  number 5
print("ПРИМЕР НОМЕР 5 Пирамида из звёздочек")
print("======================================================================================")
height = int(input("Введите высоту пирамиды: "))
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
print("======================================================================================")


