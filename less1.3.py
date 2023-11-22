#!/usr/bin/python3.11

temperature = float(input("Введите температуру: "))

is_warm = temperature >= 25
is_cool = 15 <= temperature < 25
is_cold = temperature < 15

if is_warm:
    print("Сейчас очень тепло!")
elif is_cool:
    print("Сейчас прохладно.")
elif is_cold:
    print("Сейчас холодно.")
else:
    print("Что-то пошло не так.")

