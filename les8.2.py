#!/usr/bin/python3

#Задание номер 5
stud1 = ((4, "Евген"), (5, "Данила"), (3, "Влад"), (3, "Константин"), (4, "Анатолий"))

score = int(input("Введите оценку (от 1 до 5), чтобы узнать кто её получил из студентов: "))

students_with_score = []

for student in stud1:
    if student[0] == score:
        students_with_score.append(student[1])

if students_with_score:
    print("Имена студентов с оценкой {}: {}".format(score, ", ".join(students_with_score)))
else:
    print("Нет студентов с оценкой {}.".format(score))

print('---------------------------------------------------------------------------------')

#Задание номер 6

n_chetnii = list(range(0,20,2))
print(n_chetnii)

n_vse =list(range(0,20,1))
print(n_vse)

for x in n_vse:
    if x in n_chetnii:
        print("Это число чётное:     " + str(x))
    else:
        print("Это число НЕ чётное:  " + str(x))
        
print('---------------------------------------------------------------------------------')


#задание номер 7

n_vse =list(range(0,20,1))
zna = 0
for num in n_vse:
    zna = zna + num **2
print("Сумма квадратов всех чисел: " + str(zna))
print('---------------------------------------------------------------------------------')


#задание номер 8

rows = 10
cols = 10

multiplication_table = []

for i in range(1, rows + 1):
    row = []  
    for j in range(1, cols + 1):
        row.append(i * j)  
    multiplication_table.append(row) 

for row in multiplication_table:
    print(row)
    
print('---------------------------------------------------------------------------------')    


    
