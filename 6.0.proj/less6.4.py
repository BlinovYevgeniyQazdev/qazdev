#!/usr/bin/python3

import turtle

# Создаем экран для рисования
screen = turtle.Screen()
screen.bgcolor("white")

# Создаем черепашку для рисования
tree = turtle.Turtle()
tree.speed(1)  # Устанавливаем скорость рисования (можете изменить)

# Функция для рисования ветвей ёлки
def draw_branch(branch_length, t):
    if branch_length > 5:
        # Рисуем текущую ветвь
        t.forward(branch_length)

        # Правая ветвь
        t.right(20)
        draw_branch(branch_length - 15, t)

        # Возвращаемся к начальной точке
        t.left(40)
        draw_branch(branch_length - 15, t)

        # Возвращаемся к начальной точке и делаем шаг назад
        t.right(20)
        t.backward(branch_length)

# Начальная позиция для ёлки
tree.penup()
tree.setpos(0, -200)
tree.pendown()

# Рисуем ёлку
draw_branch(100, tree)

# Закрыть окно при клике
screen.exitonclick()

