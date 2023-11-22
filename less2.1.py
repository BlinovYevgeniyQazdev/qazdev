#!/usr/bin/python3.11

#Вводя email через input нам выводит текст до символа @
email=input("Введите ваш адресс электронной почты: ")
username = email.split('@')[0]
print("Имя:", username)
