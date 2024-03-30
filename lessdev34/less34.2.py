#!/usr/bin/python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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

# Задание 5: Применение функций
# 1. Увеличить GPA каждого студента на 0.5.
students['GPA'] += 0.5

# Задание 6: Сортировка данных
# 1. Отсортировать студентов по возрасту по убыванию.
students_sorted_by_age_desc = students.sort_values(by='Age', ascending=False)

# 2. Отсортировать студентов по GPA по возрастанию.
students_sorted_by_gpa_asc = students.sort_values(by=['GPA', 'Age'])

# Задание 7: Сохранение данных
# Сохранение полученного DataFrame в файл CSV.
# Сохранение полученного DataFrame в файл CSV.
csv_file = 'students.csv'  # Путь к файлу в текущей директории
students.to_csv(csv_file, index=False)

print("\nDataFrame сохранен в файл CSV: students.csv")




print("\nСтуденты, отсортированные по убыванию возраста:")
print(students_sorted_by_age_desc)

print("\nСтуденты, отсортированные по возрастанию GPA и возрасту:")
print(students_sorted_by_gpa_asc)

print("\nDataFrame сохранен в файл CSV: students.csv")

# Построим визуализацию распределения GPA студентов
sns.histplot(data=students, x='GPA', kde=True)
plt.show()  # Отображаем график

csv_file  # Возвращаем путь к файлу для доступа к нему пользователем

