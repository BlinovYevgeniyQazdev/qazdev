#!/usr/bin/python3

#1 Программа номер 1
print("===============================================")
print("Программа№1 ПРОВЕРКА НА ЧЁТНОСТЬ И ПОЛОЖИТЕЛЬНОСТЬ")

#2 Ввод числа через метод input
number = int(input("Введите число: "))


if number % 2 == 0:
    print(f"Число {number} четное.")
else:
    print(f"Число {number} нечетное.")

if number > 0:
    print(f"Число {number} положительное.")
else:
    print(f"Число {number} отрицательное.")
    
print("===============================================")


#4 Программа номер 2
print("===============================================")
print("Программа№ ВИСОКОСНЫЙ ГОД")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Введите год: "))

if is_leap_year(year):
    print(f"{year} високосный год")
else:
    print(f"{year} не високосный год")

print("===============================================")


