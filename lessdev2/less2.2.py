#!/usr/bin/python3.11

#Программа по отбору идельного кандидата  для борьбы Сумо
print("Эй другалёк! Хочешь узнать насколько хорошо ты подходишь для борьбы Сумо??? \nЭта программа определит твою судьбу и вынесет тебе вердикт!!!")

# Получите значение  рост вес
ves = float(input("Мисье, введите ваш вес в килограммах: "))
rost = float(input("А теперь твой рост, указать значение в сантиметрах: "))

#Опеделнеие коэфицента массы тела на основе полученных данных
temp = float(ves/rost)

#Уведомление о выводе результатов
print("Мы проанализровали твою генетику, и вот что хотим тебе сообщить!")


# Проверьте условия и выведите соответствующий результат
if temp < 0.33:
    print("Дружище что-то ты худоват, тебе бы покушать и подкчаться.\nСумо не идеальный выбор для тебя, займись чем-то другим...")
elif 0.33 <= temp <= 0.45:
    print("Другалёк у тебя нормальный вес, ты просто Апполон в мире людей!\nНо для Сумо ты всё ещё маловат.")
elif 0.45 <= temp <= 0.50:
    print("Оооу да перед нами здоровый Буйвол! Ты крепкий малый, у тебя руки здоровые, ноги... \nКушай больше риса и у тебя есть все шансы!")
elif 0.50 <= temp <= 3:
    print("Мы с гордостью сообщаем вам, вы идеальный кандидат, у вас хорошые гены, вы здоровый как Пельмень и это хорошо!")
else:
    print("Вы настолько могучи и тяжелы, что мир рухнул под вашей тяжестью!!! \n Вы титан!")


#Вывод статистики
stats = f"Подведём итоги: \nТвой вес другалёк {ves} килограмм а рост {rost} сантиметров.\nТвой индекс массы тела {ves / rost} имеeт такое значение."
print(stats)