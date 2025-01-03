import time
import random
import pygame

#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
SC_Width = 800
SC_Height = 600
SC = pygame.display.set_mode((SC_Width, SC_Height), pygame.FULLSCREEN)  # Задаём размер игрового поля.

#обновляем дисплей
pygame.display.update()
#caption для окна дисплея
pygame.display.set_caption('Работа с классом RECT и поверхностями') #Добавляем название игры.
pygame.display.set_icon(pygame.image.load("my_icon.png")) # иконка программы

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
GROUND_COLOR = (100, 100, 100)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()


jump_force = 25     # сила прыжка
move = jump_force+1
hero_go_speed = 10 # скорость движения персонажа

#создаем землю
ground_width = SC_Width
ground_height = 30
ground = pygame.Surface((ground_width, ground_height))  # поверхность земли
ground.fill(GROUND_COLOR) # цвет земли
ground_rect = ground.get_rect(x=0, y=SC_Height - ground_height)
#создаем персонажа  - пока это прямоугольник
my_hero_width = 30
my_hero_height = 45
my_hero = pygame.Surface((my_hero_width, my_hero_height))  # персонаж - это поверхность
my_hero.fill(BLUE_COLOR) # цвет персонажа
my_hero_rect = my_hero.get_rect(centerx=SC_Width // 2) # устанавливаем центр персонажа по X в центре экрана
my_hero_rect.bottom = ground_rect.y #устанавливаем нижнюю часть героя по верху земли



while True:
    #обрабатываем выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    ''''обрабатываем нажатие клавиш стрелок - движение персонажа
    если уперлись в границы экрана, то дальше не жвигаемся'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_hero_rect.x -= hero_go_speed
        #уперлись в левую границу экрана
        if my_hero_rect.x < 0:
            my_hero_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        my_hero_rect.x += hero_go_speed
        # уперлись в левую границу экрана
        if my_hero_rect.x > SC_Width - my_hero_rect.width:
            my_hero_rect.x = SC_Width - my_hero_rect.width
    # если нажат пробел и герой стоит на уровне земли- то прыжок
    if keys[pygame.K_SPACE] and ground_rect.y == my_hero_rect.bottom:
        move = -jump_force # устанавливаем переменную прыжка в начальное состояние, начинаем с минуса
    #обрабатываем прыжок
    if move <= jump_force: # пока не достигнем положительного значения move совершаем прыжок, причем сначала bootom героя увеличивается, затем уменьшается
        if my_hero_rect.bottom + move < ground_rect.y:
            # скорость прыжка регулируется изменением bottom персонажа
            my_hero_rect.bottom += move # сначала скорость вверх большая, поскольку была с минусом
            if move < jump_force: # пока скорость не приравнялась к jump_force мы ее прибавляем
                move += 1
        else:
            my_hero_rect.bottom = ground_rect.y
            move = jump_force + 1 # чтобы перемещение по прыжку больше не срабатывало

    SC.fill(WHITE_COLOR)
    SC.blit(my_hero, my_hero_rect)
    SC.blit(ground, ground_rect)
    pygame.display.update()
    clock.tick(FPS)