import pygame
from class_animals import Animals
#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
SC_Width = 800
SC_Height = 600
SC = pygame.display.set_mode((SC_Width, SC_Height))  # Задаём размер игрового поля., pygame.FULLSCREEN

#обновляем дисплей
pygame.display.update()
#caption для окна дисплея
pygame.display.set_caption('Спрайты') #Добавляем название игры.
pygame.display.set_icon(pygame.image.load("images/my_icon.png")) # иконка программы

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)


FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()


jump_force = 25     # сила прыжка
move = jump_force+1
hero_go_speed = 10 # скорость движения персонажа

#создаем землю - bottom для героя
ground_height = 30
my_hero_bottom = SC_Height - ground_height

#создаем персонажа  - пока это прямоугольник
my_hero_width = 75
my_hero_height = 100

SC_background = pygame.image.load("images/background.jpg").convert()  # картинка - это тоже поверхность
SC_background_rect = SC_background.get_rect(width=SC_Width, height=SC_Height)

my_hero_surf = pygame.image.load("images/my_hero_giraf.png").convert_alpha()  # картинка - это тоже поверхность
my_hero_left = my_hero_surf
my_hero_right = pygame.transform.flip(my_hero_surf,1,0)   # 1 и 0 трансформация по горизонтали и вертикали соотвественно

my_hero = my_hero_left

my_hero_rect = my_hero.get_rect(centerx=SC_Width // 2, width=my_hero_width, height=my_hero_height) # устанавливаем центр персонажа по X в центре экрана и другие параметры
my_hero_rect.bottom = my_hero_bottom #устанавливаем нижнюю часть героя по верху земли

f = pygame.font.SysFont('Arial', 24)
sc_text = f.render('ЖИРАФ ЗИМОЙ НА ПРОГУЛКЕ!', 1, RED_COLOR, GREEN_COLOR)
sc_text_rect = sc_text.get_rect(centerx=SC_Width//2, top=0)

#----- определяме падающих животных сверху экрана--------------
MyAnimals = pygame.sprite.Group()
MyAnimals.add(Animals(SC_Width//2 + 100, 1, 'images/bear.png'),
                    Animals(SC_Width//2-100, 3, 'images/coco.png'),
                    Animals(SC_Width//2 + 300, 2, 'images/fox.png'),
                    Animals(SC_Width//2 - 150, 1, 'images/cat.png'))

while True:
    #обрабатываем выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    ''''обрабатываем нажатие клавиш стрелок - движение персонажа
    если уперлись в границы экрана, то дальше не жвигаемся'''
    old_key = pygame.K_LEFT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_hero = my_hero_left
        my_hero_rect.x -= hero_go_speed
        #уперлись в левую границу экрана
        if my_hero_rect.x < 0:
            my_hero_rect.x = 0
    if keys[pygame.K_RIGHT]:
        my_hero = my_hero_right
        my_hero_rect.x += hero_go_speed
        # уперлись в левую границу экрана
        if my_hero_rect.x > SC_Width - my_hero_rect.width:
            my_hero_rect.x = SC_Width - my_hero_rect.width
    # если нажат пробел и герой стоит на уровне земли- то прыжок
    if keys[pygame.K_SPACE] and my_hero_bottom == my_hero_rect.bottom:
        move = -jump_force # устанавливаем переменную прыжка в начальное состояние, начинаем с минуса
    #обрабатываем прыжок
    if move <= jump_force: # пока не достигнем положительного значения move совершаем прыжок, причем сначала bootom героя увеличивается, затем уменьшается
        if my_hero_rect.bottom + move < my_hero_bottom:
            # скорость прыжка регулируется изменением bottom персонажа
            my_hero_rect.bottom += move # сначала скорость вверх большая, поскольку была с минусом
            if move < jump_force: # пока скорость не приравнялась к jump_force мы ее прибавляем
                move += 1
        else:
            my_hero_rect.bottom = my_hero_bottom
            move = jump_force + 1 # чтобы перемещение по прыжку больше не срабатывало




    SC.blit(SC_background, SC_background_rect)
    SC.blit(my_hero, my_hero_rect)
    SC.blit(sc_text, sc_text_rect)

    # выводим сразу все спрайты
    MyAnimals.draw(SC)
    # обновляем сразу все спрайты
    MyAnimals.update(SC_Height)


    pygame.display.update()
    clock.tick(FPS)