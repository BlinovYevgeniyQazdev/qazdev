#!/usr/bin/python3.11

##Задание номер 1
genres = {
    "Комедия": ["Как достать соседа", "Сваты", "Мальчишник в вегасе"],
    "Боевик": ["Крепкий орешек", "Терминатор", "Хищник"],
    "Ужасы": ["Бездна", "Пила", "Обитель зла"],
    "Драма": ["Титаник"]
}

def add_movie_to_genre():
    genre_choice = input("Выберите жанр из доступных: Комедия, Боевик, Ужасы, Драма: ")
    if genre_choice in genres:
        movie = input(f"Введите название фильма для жанра '{genre_choice}': ")
        genres[genre_choice].append(movie)
        print(f"Фильм '{movie}' успешно добавлен к жанру '{genre_choice}'.")
    else:
        print("Неверный выбор жанра. Попробуйте снова.")

# Пример использования
add_movie_to_genre()

# Вывести обновленные жанры
print(genres)

##Задание номер 2
students = {
    'Константин': {'Информатика': 98, 'Математика': 80, 'Физика': 60},
    'Евгений': {'Информатика': 93, 'Математика': 75, 'Физика': 55},
    'Димасик': {'Информатика': 66, 'Математика': 85, 'Физика': 70}
}

def find_average_grades(students_dict):
    average_grades = {}
    for student, grades in students_dict.items():
        average = sum(grades.values()) / len(grades)
        average_grades[student] = average
    return average_grades

average_grades = find_average_grades(students)
for student, average in average_grades.items():
    print(f'Средний балл {student}: {average:.2f}')

find_average_grades(students)

 ##Задание номер 3
rows = 4
columns = 4
counter = 1
matrix = [[counter + columns * i + j for j in range(columns)] for i in range(rows)]
scalar = 3
scaled_matrix = [[element * scalar for element in row] for row in matrix]
for row in scaled_matrix:
    print(row)

##Задание номер 4

autors = {
    "Пушкин": {
        "Матрица": "Матрица - написана Пушкиным после злополучной дуэли с Дантесом",
        "Шрек2": "Шрек2 - классика принесшая автору успех колоссального масштаба"
    },
    "Кунанбаев": {
        "Терминатор": "Терминатор - роман эпопея, ставший культовым, любим многоими поклениями",
        "ЛюдиХ": "ЛюдиХ - Романтическа драмма о неразделнной порции картошки фри"
    }
}

target = input("Введите автора:")
for item in autors:
    if target in item:
        print(autors[item])

##Задание номер 5

def coordinates_sum(x, y, z):
    coordinates_list = [x, y, z]
    total_sum = sum(coordinates_list)
    return total_sum

# Пример использования
a = 15
b = 25
c = 35
result = coordinates_sum(a, b, c)
print(result)





