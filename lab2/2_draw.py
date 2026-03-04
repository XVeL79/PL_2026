import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

DARK_GRAY = (20, 20, 30)
GRAY = (60, 60, 70)
LIGHT_GRAY = (150, 150, 160)
WHITE_GRAY = (220, 220, 230)
YELLOW_GRAY = (180, 180, 150)
BLUE_GRAY = (100, 100, 150)

screen.fill(DARK_GRAY)

# Луна
circle(screen, LIGHT_GRAY, (700, 100), 60)

# Облака
ellipse(screen, GRAY, (50, 50, 120, 40))
ellipse(screen, GRAY, (300, 80, 150, 50))
ellipse(screen, GRAY, (550, 40, 140, 45))

# Дом
rect(screen, LIGHT_GRAY, (200, 250, 300, 250))
polygon(screen, GRAY, [(200, 250), (350, 150), (500, 250)])

# Балкон
rect(screen, GRAY, (380, 280, 100, 40), 2)
line(screen, GRAY, (380, 300), (480, 300), 2)

# Окна первого этажа
rect(screen, DARK_GRAY, (230, 360, 50, 70))   # левое
rect(screen, DARK_GRAY, (320, 360, 50, 70))   # среднее
rect(screen, YELLOW_GRAY, (410, 360, 50, 70)) # правое (свет)

# Призрак
ellipse(screen, WHITE_GRAY, (550, 350, 100, 130))
circle(screen, BLUE_GRAY, (580, 390), 10)
circle(screen, BLUE_GRAY, (620, 390), 10)

pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()