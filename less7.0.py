#!/usr/bin/python3.11

#Задание номер 1 функция для вычисления факториала числа
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

number = int(input("Введите ваше число: "))
print(factorial(number))
print("-------------------------------------------------------------------------")

#Задание номер 2
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    choice = input("Выберите опцию:\n1. Конвертировать из Цельсия в Фаренгейт\n2. Конвертировать из Фаренгейта в Цельсий\nВаш выбор (1/2): ")

    if choice == '1':
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} градусов Цельсия равно {fahrenheit} градусов Фаренгейта.")
    elif choice == '2':
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} градусов Фаренгейта равно {celsius} градусов Цельсия.")
    else:
        print("Неправильный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
print("-------------------------------------------------------------------------")

#Задание номер 3

# Функция для нахождения наибольшего общего делителя (НОД) двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для нахождения НОК двух чисел
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Ввод двух чисел от пользователя
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Вызов функции для нахождения НОК и вывод результата
result = lcm(num1, num2)
print(f"Наименьшее общее кратное {num1} и {num2} равно {result}")

print("-------------------------------------------------------------------------")

#Задание номер 4

def is_palindrome(number):
    # Преобразуем число в строку для сравнения символов
    num_str = str(number)

    # Сравниваем строку с её инвертированной версией
    if num_str == num_str[::-1]:
        return True
    else:
        return False


# Функция для получения числа от пользователя
def get_user_input():
    while True:
        try:
            number = int(input("Введите число: "))
            return number
        except ValueError:
            print("Пожалуйста, введите целое число.")


if __name__ == "__main__":
    number = get_user_input()
    if is_palindrome(number):
        print(f"{number} является палиндромом.")
    else:
        print(f"{number} не является палиндромом.")

print("-------------------------------------------------------------------------")


#Задание номер 5

def calculate_total_amount(principal, months):
    interest_rate = 0.05  # 5% процентная ставка

    # Итерация через каждый месяц и применение процентов
    for _ in range(months):
        principal += principal * interest_rate

    return principal


# Введите начальную сумму и количество месяцев
principal = float(input("Введите начальную сумму: "))
months = int(input("Введите количество месяцев: "))

total_amount = calculate_total_amount(principal, months)
print(f"Через {months} месяцев вам нужно вернуть: {total_amount:.2f} тенге")






