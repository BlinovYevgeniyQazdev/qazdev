#!/usr/bin/python3.11

#Example number 1
print("ПРИМЕР НОМЕР 1")
print("======================================================================================")
for i in range(5):
    print(i)
print("======================================================================================")

#Example number 2
print("ПРИМЕР НОМЕР 2")
print("======================================================================================")
cities = ["Алмата","Караганда","Астана"]
for city in cities:
    print("Сейчас перебирается город", city)
print("======================================================================================")

# Example number 3
print("ПРИМЕР НОМЕР 3")
print("======================================================================================")
words = "Меня зовут Билли Херрингтон!!!"
for sigt in words:
    print("РАЗБОРЧИК: ", sigt)
print("======================================================================================")

# Example number 4
print("ПРИМЕР НОМЕР 4")
print("======================================================================================")
sum=0
num = 1
while num <= 100:
    sum += num
    num += 2
print("Сумма нечетных чисел:", sum)
print("======================================================================================")

# Example number 5
print("ПРИМЕР НОМЕР 5")
print("======================================================================================")
# Запрашиваем у пользователя ввод числа
n = int(input("Введите число: "))
# Используем цикл for для вывода чётных чисел от 0 до введенного числа
for i in range(0, n + 1, 2): #разбор того что написано в скобках первое это откуда мы начинаем, второе до какого числа идём, треть с каким шагом
    print(i)
print("======================================================================================")

# Example number 6
print("ПРИМЕР НОМЕР 6")
print("======================================================================================")
chis = int(input("Введите число: "))
sur=0
num = 1
while num <= chis:
    sur += num
    num += 1
print("Сумма чисел до заданного числа:", sur)
print("======================================================================================")












