import random
import pygame
from random import randint
from class_animals import Animals
# размеры падающих животных
animal_width = 75
animal_height = 75

#инициализируем звуки в pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
SC_Width = 1920
SC_Height = 1080
SC = pygame.display.set_mode((SC_Width, SC_Height))  # Задаём размер игрового поля., pygame.FULLSCREEN

#инициализация музыки
pygame.mixer.music.load("sounds/background.mp3")
#запуск с бесконечным повторением
pygame.mixer.music.play(-1)
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
FPS_giraf = 3 # в какое число кадров менять жирафа - движение тела
clock = pygame.time.Clock()


jump_force = 35     # сила прыжка
move = jump_force+1
hero_go_speed = 15 # скорость движения персонажа

#создаем землю - bottom для героя
ground_height = 100
my_hero_bottom = SC_Height - ground_height

#создаем персонажа  - пока это прямоугольник
my_hero_width = 121
my_hero_height = 261
# очки игры
game_score = 0
score_in = 0
all_animals_count = 0


SC_background = pygame.image.load("images/background.jpg").convert()  # фон игры
SC_background_rect = SC_background.get_rect(width=SC_Width, height=SC_Height)  # фон снизу, перекрывающий персонажа
ground = pygame.image.load("images/ground.png").convert_alpha()  #
ground_rect = SC_background.get_rect(width=SC_Width, height=SC_Height)

my_hero_surf1 = pygame.image.load("images/my_hero_giraf.png").convert_alpha()  # картинка персонажа
my_hero_surf2 = pygame.image.load("images/my_hero_giraf2.png").convert_alpha()  # еще картинка персонажа (для имитации движения)
my_hero_left1 = my_hero_surf1
my_hero_right1 = pygame.transform.flip(my_hero_surf1,1,0)   # 1 и 0 трансформация по горизонтали и вертикали соотвественно
my_hero_left2 = my_hero_surf2
my_hero_right2 = pygame.transform.flip(my_hero_surf2,1,0)   # 1 и 0 трансформация по горизонтали и вертикали соотвественно

my_hero = my_hero_left1 # первоначальная (по умолчанию) поверхность персонажа

my_hero_rect = my_hero.get_rect(centerx=SC_Width // 2, width=my_hero_width, height=my_hero_height) # устанавливаем центр персонажа по X в центре экрана и другие параметры
my_hero_rect.bottom = my_hero_bottom #устанавливаем нижнюю часть героя по верху земли

f = pygame.font.Font('fonts/Bubblez_Graffiti.ttf', 48)
sc_text = f.render('SKYLINETMK FIRST GAME!', 1, RED_COLOR, GREEN_COLOR)
sc_text_rect = sc_text.get_rect(centerx=SC_Width//2, top=0)

# количество очков сверху
def Score():
    image_score = pygame.image.load('images/score.png').convert_alpha()
    f = pygame.font.Font('fonts/Bubblez_Graffiti.ttf', 38)
    sc_text = f.render(f'    Очков: {game_score}' , 1, BLUE_COLOR, WHITE_COLOR)
    SC.blit(sc_text, sc_text.get_rect(left=0, top=5))
    SC.blit(image_score, image_score.get_rect(left=0, top=5))

    image_in = pygame.image.load('images/animals_in.png').convert_alpha()
    sc_text = f.render(f'    Поймал: {score_in}' , 1, WHITE_COLOR, GREEN_COLOR)
    SC.blit(sc_text, sc_text.get_rect(left=0, top=45))
    SC.blit(image_in, image_in.get_rect(left=0, top=45))

    image_out = pygame.image.load('images/animals_out.png').convert_alpha()
    sc_text = f.render(f'    Убежало: {all_animals_count - score_in - len(MyAnimals)}' , 1, WHITE_COLOR, RED_COLOR)
    SC.blit(sc_text, sc_text.get_rect(left=0, top=85))
    SC.blit(image_out, image_out.get_rect(left=0, top=85))

def Stage(stageNumber, x, y, x2, y2):
    f = pygame.font.Font('fonts/Bubblez_Graffiti.ttf', 35)
    sc_text = pygame.transform.rotate((f.render(f'ИГРА  {stageNumber}', 1, WHITE_COLOR)), 15)
    SC.blit(sc_text, sc_text.get_rect(center=(x, y)))
    sc_text = f.render('NEXT', 1, WHITE_COLOR)
    SC.blit(sc_text, sc_text.get_rect(center=(x2, y2)))

#----- определяме падающих животных сверху экрана в виде словаря--------------
MyAnimals_images = ({'image':'bear.png','sound':'1.ogg','score': 4},
                    {'image':'cat.png','sound':'2.ogg','score': 1},
                    {'image':'coco.png','sound':'3.ogg','score': 2},
                    {'image':'cow.png','sound':'4.ogg','score': 2},
                    {'image':'dog.png','sound':'5.ogg','score': 1},
                    {'image':'el.png','sound':'6.ogg','score': 5},
                    {'image':'fox.png','sound':'7.ogg','score': 3},
                    {'image':'hamster.png','sound':'8.ogg','score': 3},
                    {'image':'lion.png','sound':'9.ogg','score': 5},
                    {'image':'rabbit.png','sound':'10.ogg','score': 4})
MyAnimals_surf = [pygame.image.load('images/'+AnimalPath['image']).convert_alpha() for AnimalPath in MyAnimals_images]

MyAnimals_sound = [pygame.mixer.Sound('sounds/'+AnimalSound['sound']) for AnimalSound in MyAnimals_images]



MyAnimals = pygame.sprite.Group()

# функция создания случайного падающего животного
def createAnimal(group):
    global all_animals_count, animal_width, animal_height
    indx = randint(0, len(MyAnimals_surf) - 1) # случайное животное из набора поверхностей
    x = randint(animal_width, SC_Width - animal_width)
    speed = randint(1, 5) # скорость случайная
    all_animals_count += 1
    return Animals(animal_width, animal_height, x, speed, MyAnimals_images[indx]['score'], MyAnimals_surf[indx], MyAnimals_sound[indx], group)
#контроль столкновения RECTов персонажа и падающих животных
def AnimalsOnGiraf():
    global game_score
    global score_in
    for animal in MyAnimals:
        if my_hero_rect.collidepoint(animal.rect.center):
            game_score += animal.score
            score_in += 1
            animal.sound.play()
            animal.kill()


# создаем первого животного
createAnimal(MyAnimals)


# устанавливаем пользовательский таймер, по нему будем создавать новых животных
pygame.time.set_timer(pygame.USEREVENT, 1000)
myHeroCadr = 0 # количество прошедших кадров на одну картинку героя

while True:
    #обрабатываем выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            createAnimal(MyAnimals)
    ''''обрабатываем нажатие клавиш стрелок - движение персонажа
    если уперлись в границы экрана, то дальше не жвигаемся'''
    old_key = pygame.K_LEFT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if (myHeroCadr > FPS_giraf):
            my_hero = random.choice([my_hero_left1, my_hero_left2])
            myHeroCadr = 0
        my_hero_rect.x -= hero_go_speed
        #уперлись в левую границу экрана
        if my_hero_rect.x < 0:
            my_hero_rect.x = 0
    if keys[pygame.K_RIGHT]:
        if (myHeroCadr > FPS_giraf):
            my_hero = random.choice([my_hero_right1, my_hero_right2])
            myHeroCadr = 0
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
    Stage(1, 320, 810, 1500, 750)

    SC.blit(my_hero, my_hero_rect)
    SC.blit(sc_text, sc_text_rect)

    # выводим сразу все спрайты
    MyAnimals.draw(SC)
    # обновляем сразу все спрайты
    MyAnimals.update(SC_Height, ground_height)
    # выводим траву, чтоб поверх персонаж аона была
    SC.blit(ground, ground_rect)

    Score()
    pygame.display.update()
    myHeroCadr += 1
    # ловим пойманных животных
    AnimalsOnGiraf()
    clock.tick(FPS)