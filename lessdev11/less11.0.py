#!/usr/bin/python3

##Задание номер 1
import math

r = 6
pi = math.pi  # Use math.pi for a more accurate value of pi
S = pi * math.pow(r, 2)
print(f'Площадь круга равна {S}')

##Задание номер 2
def is_prime(number):
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

number1 = 42
if is_prime(number1):
    print(f"{number1} - это простое число.")
else:
    print(f"{number1} - не является простым числом.")

##задание номер 3
def area_triangle(length, height):
    S = 0.5 * (length * height)
    print(f'Площадь треугольника со сторонами {length} и {height} равна {S}')

length = int(input('Введите длину треугольника:'))
height = int(input('Введите высоту треугольника:'))
area_triangle(length, height)

##задание номер 4
import datetime

current_date7 = datetime.datetime.today() + datetime.timedelta(days=7)
print(f'Через 7 дней будет {current_date7}')


##задание номер 5
from datetime import date

first_date = date(2023, 10, 2)
second_date = date(2023, 10, 30)

def delta(first_date, second_date):
    delta = second_date - first_date
    print(delta)

delta(first_date, second_date)


##задание номер 6
def input_date(year, mouth, day):
    дата = datetime.date(year, mouth, day)
    day_of_week = дата.strftime("%A")
    return day_of_week

year = int(input("Введите год (например, 2023): "))
mouth = int(input("Введите месяц (1-12): "))
day = int(input("Введите день (1-31): "))

day_of_week = input_date(year, mouth, day)
print(f"День недели для {day}.{mouth}.{year}: {day_of_week}")


##задание номер 8
import random

def random_name(rand):
    random.shuffle(rand)
    generic_name = ''.join(map(str, rand))
    print('Подобранное имя', generic_name)

rand = ['a', 'd', 'o', 12, 55, 'f']
random_name(rand)


##задание номер 9
import random

vikroty = ['Славик', 'Костя', 'Влад', 'Евген', 'Данила']
print(random.choice(vikroty))

##задание номер 10
import time

for i in range(60):
    currenttime = time.localtime()
    timestamp = time.strftime('%H:%M:%S', currenttime)
    time.sleep(1)
    print(timestamp)

##задание номер 11
import time

def current_time():
    currenttime = time.localtime()
    timestamp = time.strftime('%H:%M:%S:%p', currenttime)
    print(timestamp)

current_time()






