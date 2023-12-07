#!/usr/bin/python3

#Пример номер 1
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print()
print("------------------------------------")   

#Пример 2
size = 5
for i in range(size):
    for j in range(i+1):
        print("*",end="")
    print()
    
for i in range(size, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print("------------------------------------")   

#пример 3
numbers=[5, 10, 15, 20, 25, 30, 35, 40]
for num in numbers:
    if num > 15:
        print(num, "больше 15")
    else:
        print( num, "меньше 15")
print("------------------------------------")

#пример 4
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums=[]
for num in nums:
    if num % 2 ==0:
        even_nums.append(num)
print("Чётные числа:",even_nums)
print("------------------------------------")

#прмер 5
numss=[12, 45, 79, 34, 56]
max_value=numss[0]
for num in numss:
    if num > max_value:
        max_value = num
print("Максимальное значение:", max_value)
print("------------------------------------")
               
