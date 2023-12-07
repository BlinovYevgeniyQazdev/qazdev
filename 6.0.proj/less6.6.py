#!/usr/bin/python3

import pygame

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры экрана и клеток
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = SCREEN_WIDTH // 8

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Шахматная доска')

# Основной игровой цикл
running = True
for row in range(8):
    for col in range(8):
        color = WHITE if (row + col) % 2 == 0 else BLACK
        pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Завершение Pygame
pygame.quit()

