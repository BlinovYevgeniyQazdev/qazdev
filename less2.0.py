#!/usr/bin/python3.11

#Задание 1 #Считаем количество сисмволов в переменной name с помошью len

name = "Yevgeniy"
count = len(name)
print(count)

#Задание 2 #Вывод слов из переменной text в отельные разделенные слова

text = "DHCP англ. Dynamic Host Configuration Protocol  сетевой протокол, позволяющий сетевым устройствам автоматически получать IP-адрес"
words = text.split()
print(words)

#Задание 3 #Изменение фразы методом replace() 

fras="Давай беги быстрее! Усэйн Болт, я знаю ты можешь это!!!"
super_fras=fras.replace("Усэйн Болт", "Беги, Лес, беги! Лес, которым управляют!")
print(super_fras)
