#!/usr/bin/python3

#Домашнее задание номер 3
num = int(input("Введите число: "))
for i in range(1, num + 1):
    if i % 3 == 0:
        print(i)
print("---------------------------------------")

#Домашнее задание номер 4

numbers = [1, 5, -10, 15, -20, 25, -30]

sum_positive = 0
count_positive = 0

for num in numbers:
    if num > 0:
        sum_positive += num
        count_positive += 1

if count_positive > 0:
    average = sum_positive / count_positive
else:
    average = 0

print("Среднее арифметическое положительных чисел в списке:", average)

#Домашнее задание номер 5
def draw_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
        
tree_height = 5
draw_tree(tree_height)
print("------------------------------")


#домашнее задание номер 6

baty = int(input("Введите размер половины бабочки: "))

for i in range(1, baty + 1):
    print('X' * i + ' ' * (2 * (baty - i)) + 'o' * i)

for i in range(baty, 0, -1):
    print('x' * i + ' ' * (2 * (baty - i)) + '*' * i)



