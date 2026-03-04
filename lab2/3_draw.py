import pygame
from pygame.draw import *

pygame.init()

FPS = 30
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
# Стена
rect(screen, LIGHT_GRAY, (50, 250, 250, 200))
# Крыша
polygon(screen, GRAY, [(50, 250), (175, 190), (300, 250)])

# Балкон (2 этаж)
rect(screen, GRAY, (200, 280, 70, 25), 2)
line(screen, GRAY, (200, 295), (270, 295), 2)
for bx in range(210, 270, 15):
    line(screen, GRAY, (bx, 280), (bx, 295), 2)
# Дверь на балкон
rect(screen, DARK_GRAY, (225, 305, 25, 35))

# Окна второго этажа
rect(screen, DARK_GRAY, (90, 280, 35, 45))
rect(screen, DARK_GRAY, (140, 280, 35, 45))
line(screen, GRAY, (107, 280), (107, 325), 2)
line(screen, GRAY, (157, 280), (157, 325), 2)

# Окна первого этажа
# Левое
rect(screen, DARK_GRAY, (80, 350, 35, 55))
line(screen, GRAY, (97, 350), (97, 405), 2)
line(screen, GRAY, (80, 377), (115, 377), 2)
# Среднее
rect(screen, DARK_GRAY, (130, 350, 35, 55))
line(screen, GRAY, (147, 350), (147, 405), 2)
line(screen, GRAY, (130, 377), (165, 377), 2)
# Правое
rect(screen, YELLOW_GRAY, (180, 350, 35, 55))
line(screen, GRAY, (197, 350), (197, 405), 2)
line(screen, GRAY, (180, 377), (215, 377), 2)

# Дверь
rect(screen, DARK_GRAY, (220, 370, 40, 80))
circle(screen, GRAY, (245, 410), 4)

# ======== ДОМ 2 ========
# Стена
rect(screen, LIGHT_GRAY, (400, 230, 280, 220))
# Крыша
polygon(screen, GRAY, [(400, 230), (540, 160), (680, 230)])

# Балкон
rect(screen, GRAY, (560, 265, 80, 30), 2)
line(screen, GRAY, (560, 280), (640, 280), 2)
for bx in range(575, 640, 20):
    line(screen, GRAY, (bx, 265), (bx, 280), 2)
rect(screen, DARK_GRAY, (590, 295, 30, 40))

# Окна второго этажа
rect(screen, DARK_GRAY, (450, 265, 40, 50))
rect(screen, DARK_GRAY, (510, 265, 40, 50))
line(screen, GRAY, (470, 265), (470, 315), 2)
line(screen, GRAY, (530, 265), (530, 315), 2)

# Окна первого этажа
rect(screen, DARK_GRAY, (440, 340, 40, 60))
line(screen, GRAY, (460, 340), (460, 400), 2)
rect(screen, DARK_GRAY, (500, 340, 40, 60))
line(screen, GRAY, (520, 340), (520, 400), 2)
rect(screen, DARK_GRAY, (560, 340, 40, 60))
line(screen, GRAY, (580, 340), (580, 400), 2)

# Дверь
rect(screen, DARK_GRAY, (610, 360, 45, 90))
circle(screen, GRAY, (635, 405), 4)

# ======== ДОМ 3 ========
# Стена
rect(screen, LIGHT_GRAY, (800, 240, 260, 210))
# Крыша
polygon(screen, GRAY, [(800, 240), (930, 175), (1060, 240)])

# Балкон
rect(screen, GRAY, (950, 272, 75, 28), 2)
line(screen, GRAY, (950, 288), (1025, 288), 2)
for bx in range(962, 1025, 18):
    line(screen, GRAY, (bx, 272), (bx, 288), 2)
rect(screen, DARK_GRAY, (975, 300, 28, 38))

# Окна второго этажа
rect(screen, DARK_GRAY, (845, 272, 38, 48))
rect(screen, DARK_GRAY, (900, 272, 38, 48))
line(screen, GRAY, (864, 272), (864, 320), 2)
line(screen, GRAY, (919, 272), (919, 320), 2)

# Окна первого этажа
# Левое
rect(screen, DARK_GRAY, (835, 345, 35, 55))
line(screen, GRAY, (852, 345), (852, 400), 2)
# Среднее
rect(screen, DARK_GRAY, (885, 345, 35, 55))
line(screen, GRAY, (902, 345), (902, 400), 2)
# Правое (со светом)
rect(screen, YELLOW_GRAY, (935, 345, 35, 55))
line(screen, GRAY, (952, 345), (952, 400), 2)

# Дверь
rect(screen, DARK_GRAY, (980, 355, 42, 95))
circle(screen, GRAY, (1005, 405), 4)

# ======== 5 ПРИЗРАКОВ ========
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

# Трава/дорога внизу
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