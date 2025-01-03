import time
import random
import pygame

#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
SC_Width = 800
SC_Height = 600
SC = pygame.display.set_mode((SC_Width, SC_Height))  # Задаём размер игрового поля., pygame.FULLSCREEN

#обновляем дисплей
pygame.display.update()
#caption для окна дисплея
pygame.display.set_caption('Работа с классом RECT и поверхностями') #Добавляем название игры.
pygame.display.set_icon(pygame.image.load("my_icon.png")) # иконка программы

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

#создаем поверхности - основной элемент игр
surf1_Width = 400
surf1 = pygame.Surface((surf1_Width, 300))
surf2 = pygame.Surface((100, 20))

surf1.fill(BLUE_COLOR)
surf2.fill(RED_COLOR)

bx, by = 0, 150
x, y = int(SC_Width/2 - surf1_Width/2), 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf1.fill(BLUE_COLOR)
    #создаем поверхность 2 на первой (при этом координаты по иксу будут меняться
    surf1.blit(surf2, (bx, by))
    if bx < SC_Width:
        bx += 5
    else:
        bx = 0

    if y < SC_Height:
        y += 1
    else:
        y = 0

    SC.fill(WHITE_COLOR)
    # создаем поверхность 1 на ГЛАВНОЙ ПОВЕРХНОСТИ (при этом координаты по игрек будут меняться
    SC.blit(surf1, (x, y))
    pygame.display.update()

    clock.tick(FPS)