#!/usr/bin/python3.11

#Задание со звёздочкой
import random

#генерация числа
while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("ИГРА УГАДАЙКА!")
    print("Мисье я загадал число от 1 до 100. Попробуй его отгадать.")

    while True:
        try:
            guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Только целые числа.")
            continue

        if guess < secret_number:
            print("Мое число больше твоего числа.")
        elif guess > secret_number:
            print("Мое число меньше твоего числа.")
        else:
            print(f"Поздравляю братишка! Ты угадал число {secret_number}")
            break

    play_again = input("Хочешь ещё партию сударь? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("GAME OVER!")
