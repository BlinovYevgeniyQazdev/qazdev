#!/usr/bin/python3

# Задание номер 1
def create_students_dict():
    studenti = {
            '1' : 'Владислав',
            '2' : 'Константин',
            '3' : 'Даниил',
            '4' : 'Евгений',
            '5' : 'Анатолий',
            '6' : 'Дмитрий'
           }
    return studenti

students_dict = create_students_dict()
print(students_dict)

delit = input('Введите номер студента, которого нужно удалить: ')

if delit in students_dict:
    del students_dict[delit]
    print('Новый список студентов: ', students_dict)
else:
    print('ОШИБКА: НЕ ВЕРНЫЙ НОМЕР')
print('__________________________________________')
