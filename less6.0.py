#!/usr/bin/python3

#пример1
for i in range(2):
    for j in range(2):
        print(i, j)
print("------------------------------------")        


#пример2
x = int(input("Введите ваше число: "))
if x>5:
    if x < 15:
        print("Число X меньше 15 и больше 5")
print("------------------------------------")

#пример 3
hour = int(input("Введите который чейчас час: "))
if hour < 12:
    print("Доброе утро!")
else:
    if hour < 18:
        print("Добрй день!")
    else:
        print("Добрый вечер!")
print("------------------------------------")

#прмер 4
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
print()        


#пример 5 шахматная доска
for i in range(8):
    for j in range(8):
        if (i+j)% 2==0:
            print("■",end="")
        else:
            print("□", end="")
    print()            