import pygame
from pygame.draw import *

pygame.init()

FPS = 3
screen = pygame.display.set_mode((1200, 700))

# Цвета
DARK_GRAY = (20, 20, 30)
GRAY = (60, 60, 70)
LIGHT_GRAY = (130, 130, 140)
WHITE_GRAY = (210, 210, 220)
YELLOW_GRAY = (190, 180, 140)
BLUE_GRAY = (110, 140, 190)
DARK_BLUE_GRAY = (40, 50, 80)

screen.fill(DARK_GRAY)

# ЛУНА
circle(screen, LIGHT_GRAY, (1000, 100), 70)
circle(screen, DARK_GRAY, (1020, 80), 12)
circle(screen, DARK_GRAY, (980, 120), 10)

# ОБЛАКА
ellipse(screen, GRAY, (30, 50, 140, 50))
ellipse(screen, GRAY, (60, 30, 120, 45))
ellipse(screen, GRAY, (200, 70, 160, 55))
ellipse(screen, GRAY, (400, 40, 180, 60))
ellipse(screen, GRAY, (500, 20, 150, 50))
ellipse(screen, GRAY, (600, 60, 170, 55))
ellipse(screen, GRAY, (750, 30, 160, 50))
ellipse(screen, GRAY, (850, 60, 180, 60))
ellipse(screen, GRAY, (950, 40, 150, 45))

# ======== ДОМ 1 ========
x1, y1 = 50, 250
w1, h1 = 250, 200

# Стена
rect(screen, LIGHT_GRAY, (x1, y1, w1, h1))
# Крыша
polygon(screen, GRAY, [(x1, y1), (x1 + w1//2, y1 - 60), (x1 + w1, y1)])

# Балкон (2 этаж)
balcony_x1 = x1 + w1 - 100
rect(screen, GRAY, (balcony_x1, y1 + 30, 70, 25), 2)
line(screen, GRAY, (balcony_x1, y1 + 45), (balcony_x1 + 70, y1 + 45), 2)
for bx in range(balcony_x1 + 10, balcony_x1 + 70, 15):
    line(screen, GRAY, (bx, y1 + 30), (bx, y1 + 45), 2)
# Дверь на балкон
rect(screen, DARK_GRAY, (balcony_x1 + 25, y1 + 55, 25, 35))

# Окна второго этажа
rect(screen, DARK_GRAY, (x1 + 40, y1 + 30, 35, 45))
rect(screen, DARK_GRAY, (x1 + 90, y1 + 30, 35, 45))
line(screen, GRAY, (x1 + 57, y1 + 30), (x1 + 57, y1 + 75), 2)
line(screen, GRAY, (x1 + 107, y1 + 30), (x1 + 107, y1 + 75), 2)

# Окна первого этажа
# Левое (темное)
rect(screen, DARK_GRAY, (x1 + 30, y1 + 100, 35, 55))
line(screen, GRAY, (x1 + 47, y1 + 100), (x1 + 47, y1 + 155), 2)
line(screen, GRAY, (x1 + 30, y1 + 127), (x1 + 65, y1 + 127), 2)
# Среднее (темное)
rect(screen, DARK_GRAY, (x1 + 80, y1 + 100, 35, 55))
line(screen, GRAY, (x1 + 97, y1 + 100), (x1 + 97, y1 + 155), 2)
line(screen, GRAY, (x1 + 80, y1 + 127), (x1 + 115, y1 + 127), 2)
# Правое (со светом)
rect(screen, YELLOW_GRAY, (x1 + 130, y1 + 100, 35, 55))
line(screen, GRAY, (x1 + 147, y1 + 100), (x1 + 147, y1 + 155), 2)
line(screen, GRAY, (x1 + 130, y1 + 127), (x1 + 165, y1 + 127), 2)

# Дверь
rect(screen, DARK_GRAY, (x1 + 170, y1 + 120, 40, 80))
circle(screen, GRAY, (x1 + 195, y1 + 160), 4)

# ======== ДОМ 2 ========
x2, y2 = 400, 230
w2, h2 = 280, 220

# Стена
rect(screen, LIGHT_GRAY, (x2, y2, w2, h2))
# Крыша
polygon(screen, GRAY, [(x2, y2), (x2 + w2//2, y2 - 70), (x2 + w2, y2)])

# Балкон
balcony_x2 = x2 + w2 - 120
rect(screen, GRAY, (balcony_x2, y2 + 35, 80, 30), 2)
line(screen, GRAY, (balcony_x2, y2 + 50), (balcony_x2 + 80, y2 + 50), 2)
for bx in range(balcony_x2 + 15, balcony_x2 + 80, 20):
    line(screen, GRAY, (bx, y2 + 35), (bx, y2 + 50), 2)
rect(screen, DARK_GRAY, (balcony_x2 + 30, y2 + 65, 30, 40))

# Окна второго этажа
rect(screen, DARK_GRAY, (x2 + 50, y2 + 35, 40, 50))
rect(screen, DARK_GRAY, (x2 + 110, y2 + 35, 40, 50))
line(screen, GRAY, (x2 + 70, y2 + 35), (x2 + 70, y2 + 85), 2)
line(screen, GRAY, (x2 + 130, y2 + 35), (x2 + 130, y2 + 85), 2)

# Окна первого этажа
rect(screen, DARK_GRAY, (x2 + 40, y2 + 110, 40, 60))
line(screen, GRAY, (x2 + 60, y2 + 110), (x2 + 60, y2 + 170), 2)
rect(screen, DARK_GRAY, (x2 + 100, y2 + 110, 40, 60))
line(screen, GRAY, (x2 + 120, y2 + 110), (x2 + 120, y2 + 170), 2)
rect(screen, DARK_GRAY, (x2 + 160, y2 + 110, 40, 60))
line(screen, GRAY, (x2 + 180, y2 + 110), (x2 + 180, y2 + 170), 2)

# Дверь
rect(screen, DARK_GRAY, (x2 + 210, y2 + 130, 45, 90))
circle(screen, GRAY, (x2 + 235, y2 + 175), 4)

# ======== ДОМ 3 ========
x3, y3 = 800, 240
w3, h3 = 260, 210

# Стена
rect(screen, LIGHT_GRAY, (x3, y3, w3, h3))
# Крыша
polygon(screen, GRAY, [(x3, y3), (x3 + w3//2, y3 - 65), (x3 + w3, y3)])

# Балкон
balcony_x3 = x3 + w3 - 110
rect(screen, GRAY, (balcony_x3, y3 + 32, 75, 28), 2)
line(screen, GRAY, (balcony_x3, y3 + 48), (balcony_x3 + 75, y3 + 48), 2)
for bx in range(balcony_x3 + 12, balcony_x3 + 75, 18):
    line(screen, GRAY, (bx, y3 + 32), (bx, y3 + 48), 2)
rect(screen, DARK_GRAY, (balcony_x3 + 25, y3 + 60, 28, 38))

# Окна второго этажа
rect(screen, DARK_GRAY, (x3 + 45, y3 + 32, 38, 48))
rect(screen, DARK_GRAY, (x3 + 100, y3 + 32, 38, 48))
line(screen, GRAY, (x3 + 64, y3 + 32), (x3 + 64, y3 + 80), 2)
line(screen, GRAY, (x3 + 119, y3 + 32), (x3 + 119, y3 + 80), 2)

# Окна первого этажа
# Левое (темное)
rect(screen, DARK_GRAY, (x3 + 35, y3 + 105, 35, 55))
line(screen, GRAY, (x3 + 52, y3 + 105), (x3 + 52, y3 + 160), 2)
# Среднее (темное)
rect(screen, DARK_GRAY, (x3 + 85, y3 + 105, 35, 55))
line(screen, GRAY, (x3 + 102, y3 + 105), (x3 + 102, y3 + 160), 2)
# Правое (со светом)
rect(screen, YELLOW_GRAY, (x3 + 135, y3 + 105, 35, 55))
line(screen, GRAY, (x3 + 152, y3 + 105), (x3 + 152, y3 + 160), 2)

# Дверь
rect(screen, DARK_GRAY, (x3 + 180, y3 + 115, 42, 95))
circle(screen, GRAY, (x3 + 205, y3 + 165), 4)


# Призрак 1
ellipse(screen, WHITE_GRAY, (20, 420, 80, 100))
circle(screen, BLUE_GRAY, (40, 450), 8)
circle(screen, BLUE_GRAY, (70, 450), 8)
circle(screen, DARK_BLUE_GRAY, (42, 452), 3)
circle(screen, DARK_BLUE_GRAY, (72, 452), 3)
arc(screen, DARK_GRAY, (40, 470, 40, 15), 0, 3.14, 2)

# Призрак 2
ellipse(screen, WHITE_GRAY, (280, 400, 90, 110))
circle(screen, BLUE_GRAY, (310, 430), 9)
circle(screen, BLUE_GRAY, (350, 430), 9)
circle(screen, DARK_BLUE_GRAY, (312, 432), 4)
circle(screen, DARK_BLUE_GRAY, (352, 432), 4)
arc(screen, DARK_GRAY, (310, 450, 40, 18), 0, 3.14, 2)

# Призрак 3
ellipse(screen, WHITE_GRAY, (450, 150, 70, 90))
circle(screen, BLUE_GRAY, (470, 180), 7)
circle(screen, BLUE_GRAY, (500, 180), 7)
circle(screen, DARK_BLUE_GRAY, (472, 182), 3)
circle(screen, DARK_BLUE_GRAY, (502, 182), 3)
arc(screen, DARK_GRAY, (470, 200, 30, 12), 0, 3.14, 2)

# Призрак 4
ellipse(screen, WHITE_GRAY, (650, 380, 85, 105))
circle(screen, BLUE_GRAY, (680, 410), 8)
circle(screen, BLUE_GRAY, (715, 410), 8)
circle(screen, DARK_BLUE_GRAY, (682, 412), 3)
circle(screen, DARK_BLUE_GRAY, (717, 412), 3)
arc(screen, DARK_GRAY, (680, 430, 35, 15), 0, 3.14, 2)

# Призрак 5
ellipse(screen, WHITE_GRAY, (1050, 350, 95, 120))
circle(screen, BLUE_GRAY, (1080, 390), 10)
circle(screen, BLUE_GRAY, (1120, 390), 10)
circle(screen, DARK_BLUE_GRAY, (1082, 392), 4)
circle(screen, DARK_BLUE_GRAY, (1122, 392), 4)
arc(screen, DARK_GRAY, (1080, 415, 45, 20), 0, 3.14, 3)

# Дорога
rect(screen, GRAY, (0, 550, 1200, 150))

pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()