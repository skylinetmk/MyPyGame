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
snake_color = (0, 0, 0)
food_color = (255, 0, 0)
dispay_mes_color = (190, 0, 0)

#стиль выводимого текста на экран при ошибках или окончании игры
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont("bahnschrift", 30)

clock = pygame.time.Clock() # для использования игрового времени (скорости игры)
snake_speed = 10 #Ограничим скорость движения змейки
snake_block = 20 #размер блока змейки


#Создадим функцию, которая будет показывать нам сообщения на игровом экране.
def display_message(msg,color):
    message_text = font_style.render(msg, True, color)
    #узнаем ширину окна с сообщением
    mesage_text_width = message_text.get_rect()[2]
    #dis.blit(message_text, [display_width/2, display_height/2])
    dis.blit(message_text, [display_width/2 - mesage_text_width/2, display_height / 2])

#Функция отображения тела змейки
def my_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

def score(score_text):
   value = score_font.render("Съедено яблок: " + str(score_text), True, yellow)
   dis.blit(value, [0, 0])

def gameLoop(): #Описываем всю игровую логику в одной функции.
    # переменная статуса игры (продолжаеся или закончена)
    game_over = False

    # закрыть игру или продолжить
    game_close = False

    snake_List = []  # Создаём список, в котором будем хранить показатель текущей длины змейки.
    Length_of_snake = 1
    global_key_go = 0


    # стартовое положение змейки - середина экрана
    snake_x = display_width / 2  # Указываем начальное значение положения змейки по оси х.
    snake_y = display_height / 2  # Указываем начальное значение положения змейки по оси y.

    snake_x_change = 0  # Создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси х.
    snake_y_change = 0  # создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси y.

    # Создаём переменную, которая будет указывать расположение еды по оси х.
    foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
    # Создаём переменную, которая будет указывать расположение еды по оси y.
    foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block


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
        for event in pygame.event.get():
            print(event)  #Выводить в терминал все произошедшие события.
            if event.type==pygame.QUIT:
                game_over = True
                game_close = False
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



        # проверяем новое значение положение головы змейки, если з апределами экрана, то окончание игры
        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change #Записываем новое значение положения змейки по оси х.
        snake_y += snake_y_change #Записываем новое значение положения змейки по оси y.
        #заливка
        dis.fill(dis_fon)
        # рисуем змейку
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
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
        score(Length_of_snake - 1)
        pygame.display.update() #обновляем дисплей

        if snake_x == foodx and snake_y == foody:  # Указываем, что в случаях, если координаты головы змейки совпадают с координатами еды, еда появляется в новом месте, а длина змейки увеличивается на одну клетку.
            foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1



        clock.tick(snake_speed) #скорость игры

    pygame.quit()
    #выходим из игры (закрытие окна при нажатии кнопки закрытия)
    quit()
gameLoop()