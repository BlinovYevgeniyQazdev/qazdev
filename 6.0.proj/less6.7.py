#!/usr/bin/python3

import pygame
import math

# Инициализация Pygame
pygame.init()

# Цвета
GREEN = (0, 255, 0)

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ёлочка')

# Основной игровой цикл
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, GREEN, [(200, 250), (185, 300), (215, 300)])
    pygame.draw.polygon(screen, GREEN, [(200, 200), (190, 250), (210, 250)])
    pygame.draw.polygon(screen, GREEN, [(200, 150), (175, 250), (225, 250)])
    pygame.draw.polygon(screen, GREEN, [(200, 100), (150, 200), (250, 200)])
    
    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
 
