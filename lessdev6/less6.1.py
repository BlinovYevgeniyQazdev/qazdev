#!/usr/bin/python3

#Домашнее задание номер 1

score = int(input("Введите вашу оценку (от 1 до 10): "))
if score >= 1 and score <= 3:
    print("Плохо")
elif score >= 4 and score <= 6:  
    print("Удовлетворительно")
else:
    if score >= 7 and score <= 9:
        print("Хорошо")
    elif score == 10:
        print("Отлично")
    else:
        print("Недопустимое значение оценки!")
print("-----------------------------------------------")

#Домашнее задание номер 2
h = int(input("Введите который сейчас час(0-24): "))
if h >= 6 and h <= 12:
    print("Доброе утро!")
elif h >= 12 and h <= 18:  
    print("Добрый день!")
else:
    if h >= 18 and h <= 24:
        print("Добрый вечер!")
    elif h >= 0 and h <= 6:
        print("Спокойной ночи!")
    else:
        print("Недопустимое значение времени!")
print("-----------------------------------------------")