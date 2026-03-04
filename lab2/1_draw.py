import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Рисуем смайлик (один раз до цикла)
screen.fill(GRAY)

# Лицо
circle(screen, YELLOW, (200, 200), 150)

# Глаза (красные с черными точками)
circle(screen, RED, (130, 150), 30)
circle(screen, RED, (270, 150), 30)
circle(screen, BLACK, (130, 150), 8)
circle(screen, BLACK, (270, 150), 8)

# Злые брови
line(screen, BLACK, (80, 100), (150, 130), 6)
line(screen, BLACK, (250, 130), (320, 100), 6)

# Толстый горизонтальный рот
line(screen, BLACK, (130, 250), (270, 250), 10)

pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()