#!/usr/bin/python3

#1 Программа номер 1
print("===============================================")
print("Программа№1 МОЖЕТЕ ЛИ ВЫ УЧАВСТОВАТЬ В ФУТБОЛЬНОМ МАТЧЕ")

#2 Категории здоровья
print("Введите следующие значения:\nПолностью здоров - 5\nЗдоров с незначительными ограничениями - 4\nНездоров - 3\nБольной - 2\nИнвалидность - 1 ") 
num = int(input("Введите вашу категорию(номер): "))

#3 веедите ваш возраст
age = int(input("Введите ваш возраст: "))

#4 момент так сказать сравнения

if age > 18 and age <= 45 and (num >= 4 and num <= 5):
    print("Вы подходите по всем параметрам!")
elif age <= 18 or age > 45:
    print("Вы не проходите по возрасту")
elif num < 3:
    print("Вы не проходите по состоянию здоровья")
else:
    print("Упс, ошибка...!")