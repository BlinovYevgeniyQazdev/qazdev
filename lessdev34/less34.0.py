#!/usr/bin/python3

import pandas as pd
import seaborn as sns

# Задание 1: Создание DataFrame
students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Age': [22, 23, 21, 22, 20],
    'Gender': ['F', 'M', 'M', 'F', 'M'],
    'GPA': [3.5, 3.7, 3.2, 3.8, 3.1]
})

print("DataFrame с информацией о студентах:")
print(students)

# Задание 2: Индексация и выбор данных
# 1. Вывести столбец 'Name' для всех студентов.
print("\nИмена всех студентов:")
print(students['Name'])

# 2. Вывести только студентов женского пола.
print("\nСтуденты женского пола:")
print(students[students['Gender'] == 'F'])

# 3. Вывести информацию о студенте с наивысшим баллом GPA.
print("\nСтудент с наивысшим баллом GPA:")
print(students.loc[students['GPA'].idxmax()])

# Задание 3: Обновление данных
# 1. Увеличить возраст всех студентов на 1.
students['Age'] += 1

# 2. Обновить балл GPA для студента с наименьшим возрастом.
min_age_index = students['Age'].idxmin()
students.loc[min_age_index, 'GPA'] += 0.1

print("\nОбновленная информация о студентах:")
print(students)

# Задание 4: Добавление новых данных
# 1. Добавить нового студента к DataFrame.
new_student = pd.DataFrame({
    'Name': ['Fay'],
    'Age': [21],
    'Gender': ['F'],
    'GPA': [3.9]
})
students = pd.concat([students, new_student], ignore_index=True)

print("\nDataFrame с новым студентом:")
print(students)

# Построим визуализацию распределения GPA студентов
sns.histplot(data=students, x='GPA', kde=True)

