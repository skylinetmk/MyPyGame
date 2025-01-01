import time
import random
import pygame

#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
display_width = 800
display_height = 600
dis = pygame.display.set_mode((display_width, display_height))  # Задаём размер игрового поля.

#обновляем дисплей
pygame.display.update()
#caption для окна дисплея
pygame.display.set_caption('Змейка от skylinetmk') #Добавляем название игры.


#обозначаем цвета в rgb
yellow = (255, 255, 102)
dis_fon = (50, 190, 86)
# змея
snake_color1 = (255, 200, 90)
snake_color2 = (40, 20, 100)
snake_color_contur = (0, 40, 0)
# еда
food_color1 = (255, 0, 0)
food_color2 = (0, 0, 0)
dispay_mes_color = (190, 0, 0)
#преграда
barriers_color = (0, 0, 0)

#стиль выводимого текста на экран при ошибках или окончании игры
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont("bahnschrift", 30)

clock = pygame.time.Clock() # для использования игрового времени (скорости игры)
snake_speed_list = [10,30] #Ограничим скорость движения змейки (обычная и при зажатой клавише)
snake_speed = snake_speed_list[0] #Стартовая скорость движеня змейки

snake_block = 20 #размер блока змейки

#вводим уровень сложности (количество преград)
#input_level = input("ВВЕДИТЕ УРОВЕНЬ СЛОЖНОСТИ:(1-100): ")
input_level = 10
#Создадим функцию, которая будет показывать нам сообщения на игровом экране.
def display_message(msg,color):
    message_text = font_style.render(msg, True, color)
    #узнаем ширину окна с сообщением
    mesage_text_width = message_text.get_rect()[2]
    #dis.blit(message_text, [display_width/2, display_height/2])
    dis.blit(message_text, [display_width/2 - mesage_text_width/2, display_height / 2])

#Функция отображения тела змейки
def my_snake(snake_block, snake_list):
   i=0
   for x in snake_list:
       # змейка из квадратов
       #pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])
       #змейка из шаров, чуть ее разннобразим
       if i%2 == 0:
           pygame.draw.circle(dis, snake_color1, [x[0] + snake_block/2, x[1] + snake_block/2], snake_block/2)
           pygame.draw.circle(dis, snake_color_contur, [x[0] + snake_block / 2, x[1] + snake_block / 2], snake_block / 2, 3)
       else:
           pygame.draw.circle(dis, snake_color2, [x[0] + snake_block/2, x[1] + snake_block/2], snake_block/2  + snake_block/8)
           pygame.draw.circle(dis, snake_color_contur, [x[0] + snake_block/2, x[1] + snake_block/2], snake_block/2  + snake_block/8,  3)
       i += 1

#Функция отображения еды змейки
def my_apple(x,y):
    # pygame.draw.rect(dis, food_color, [x, y, snake_block, snake_block])
    pygame.draw.circle(dis, food_color1, [x + snake_block/2, y + snake_block/2],  snake_block/2) #само тело яблока
    pygame.draw.circle(dis, food_color2, [x + snake_block / 2, y + snake_block / 2], snake_block/2, 1) #окантовка яблока
    

#функция отображения текущего счета
def score(score_text):
   value = score_font.render("Съедено яблок: " + str(score_text), True, yellow)
   dis.blit(value, [0, 0])

#функция отрисовки преград для змейки
def my_barriers(barriers_list):
    for i in barriers_list:
        pygame.draw.rect(dis, barriers_color, [i[0], i[1], snake_block, snake_block])

#функция формирования массива преград
def barrierslist(level):
    barriers_list = []
    for i in range(level):
            barier_x = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
            barier_y = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block
            barriers_list.append([barier_x, barier_y])
    return barriers_list


#основная функиця всей игровой логики игры
def gameLoop(): #Описываем всю игровую логику в одной функции.
    # переменная статуса игры (продолжаеся или закончена)
    game_over = False

    # закрыть игру или продолжить
    game_close = False

    snake_List = []  # Создаём список, в котором будем хранить показатель текущей длины змейки.
    Length_of_snake = 1
    global_key_go = 0

    barriers_List = []

    # стартовое положение змейки - середина экрана
    snake_x = display_width / 2  # Указываем начальное значение положения змейки по оси х.
    snake_y = display_height / 2  # Указываем начальное значение положения змейки по оси y.

    snake_x_change = 0  # Создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси х.
    snake_y_change = 0  # создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси y.

    def new_food():
        # Создаём переменную, которая будет указывать расположение еды по оси х.
        foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
        # Создаём переменную, которая будет указывать расположение еды по оси y.
        foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block
        return [foodx, foody]

    # преграды
    barriers_List = barrierslist(int(input_level))
    #первоначальное появление еды
    new_food_xy = new_food()
    while new_food_xy in barriers_List:
        new_food_xy = new_food()
    foodx = new_food_xy[0]
    foody = new_food_xy[1]


    #пока игра продолжается
    while not game_over:
        # игра временно остановлена, ждем решение пользователя
        while game_close == True:
            dis.fill(dis_fon)
            display_message("Вы проиграли! Нажмите Q для выхода или С для новой игры", dispay_mes_color)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Игра продолжается
        keydown_status = 0
        global snake_speed
        for event in pygame.event.get():
            print(event)  #Выводить в терминал все произошедшие события.
            if event.type==pygame.QUIT:
                game_over = True
                game_close = False
            # отдали клавишу втрелок обратно
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                snake_speed = snake_speed_list[0] # обычное движение змейки (скорость)
            if event.type == pygame.KEYDOWN: #Добавляем считывание направления движения змеи

                # проверяем смену направления движения змейки
                if event.key == pygame.K_LEFT and global_key_go != pygame.K_RIGHT: # стрелка влево и до этого змейка не бежала вправо
                    snake_x_change = -snake_block  # Указываем шаг изменения положения змейки
                    snake_y_change = 0
                if event.key == pygame.K_RIGHT and global_key_go != pygame.K_LEFT: # стрелка вправо и до этого змейка не бежала влево
                    snake_x_change = snake_block  # Указываем шаг изменения положения змейки
                    snake_y_change = 0
                if event.key == pygame.K_UP and global_key_go != pygame.K_DOWN: # стрелка ввверх и до этого змейка не бежала вниз
                    snake_x_change = 0  # Указываем шаг изменения положения змейки
                    snake_y_change = -snake_block
                if event.key == pygame.K_DOWN and global_key_go != pygame.K_UP: # стрелка вниз и до этого змейка не бежала ввверх
                    snake_x_change = 0  # Указываем шаг изменения положения змейки
                    snake_y_change = snake_block

                # присваиваем переменной нажатие кнопки - направления движения, для того чтоб змейка не разворачивалась головой в свое же тело
                global_key_go = event.key
                # присваиваем статус нажатой клавиши на случай, если клавиша не будет отжата
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    snake_speed = snake_speed_list[1] # ускоренное движение змейки

        # проверяем новое значение положение головы змейки, если за пределами экрана, то окончание игры
        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            game_close = True
        #змейка врезалась в препятствие
        if ([snake_x, snake_y] in barriers_List):
            game_close = True

        snake_x += snake_x_change #Записываем новое значение положения змейки по оси х.
        snake_y += snake_y_change #Записываем новое значение положения змейки по оси y.
        #заливка
        dis.fill(dis_fon)
        # рисуем еду змейки
        my_apple(foodx, foody)

        # Создаём список, в котором будет храниться показатель длины змейки при движениях.
        snake_Head = []
        snake_Head.append(snake_x)  # Добавляем значения в список при изменении по оси х.
        snake_Head.append(snake_y)  # Добавляем значения в список при изменении по оси y.
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]  # Удаляем первый элемент в списке длины змейки, чтобы она не увеличивалась сама по себе при движениях.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        # рисуем змейку
        my_snake(snake_block, snake_List)
        # рисуем препятствия
        my_barriers(barriers_List)

        # выводим текущий счет съеденных яблок
        score(Length_of_snake - 1)
        pygame.display.update() #обновляем дисплей


        # Указываем, что в случаях, если координаты головы змейки совпадают с координатами еды, еда появляется в новом месте, а длина змейки увеличивается на одну клетку.
        if (snake_x == foodx and snake_y == foody):
            new_food_xy = new_food()
            foodx = new_food_xy[0]
            foody = new_food_xy[1]
            # пересоздаем координаты, если  они попадают в препятствие
            while new_food_xy in barriers_List:
                new_food_xy = new_food()
                foodx = new_food_xy[0]
                foody = new_food_xy[1]
            Length_of_snake += 1

        clock.tick(snake_speed) #скорость игры

    pygame.quit()
    #выходим из игры (закрытие окна при нажатии кнопки закрытия)
    quit()
gameLoop()