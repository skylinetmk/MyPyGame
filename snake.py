import time

import pygame
#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
display_width = 1024
display_height = 768
dis = pygame.display.set_mode((display_width, display_height))  # Задаём размер игрового поля.

#обновляем дисплей
pygame.display.update()
#caption для окна дисплея
pygame.display.set_caption('Змейка от skylinetmk') #Добавляем название игры.

#переменная статуса игры (продолжаеся или закончена)
game_over=False

#обозначаем цвета в rgb
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
message_color = (190, 233, 22)

#стиль выводимого текста на экран при ошибках или окончании игры
font_style = pygame.font.SysFont(None, 100)


#стартовое положение змейки - середина экрана
snake_x = display_width/2 #Указываем начальное значение положения змейки по оси х.
snake_y = display_height/2 #Указываем начальное значение положения змейки по оси y.

snake_x_change = 0 #Создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси х.
snake_y_change = 0 #создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси y.
clock = pygame.time.Clock() # для использования игрового времени (скорости игры)
snake_speed=15 #Ограничим скорость движения змейки

#Создадим функцию, которая будет показывать нам сообщения на игровом экране.
def display_message(msg,color):
    message_text = font_style.render(msg, True, color)
    dis.blit(message_text, [display_width/2, display_height/2])



#пока игра продолжается
while not game_over:
    for event in pygame.event.get():
        print(event)  #Выводить в терминал все произошедшие события.
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN: #Добавляем считывание направления движения змеи
            if event.key == pygame.K_LEFT: # стрелка влево
                snake_x_change = -10  # Указываем шаг изменения положения змейки
                snake_y_change = 0
            if event.key == pygame.K_RIGHT: # стрелка вправо
                snake_x_change = 10  # Указываем шаг изменения положения змейки
                snake_y_change = 0
            if event.key == pygame.K_UP: # стрелка ввверх
                snake_x_change = 0  # Указываем шаг изменения положения змейки
                snake_y_change = -10
            if event.key == pygame.K_DOWN: # стрелка вниз
                snake_x_change = 0  # Указываем шаг изменения положения змейки
                snake_y_change = 10
    # проверяем новое значение положение головы змейки, если з апределами экрана, то окончание игры
    if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
        game_over = True

    snake_x += snake_x_change #Записываем новое значение положения змейки по оси х.
    snake_y += snake_y_change #Записываем новое значение положения змейки по оси y.
    dis.fill(white)

    pygame.draw.rect(dis, black, [snake_x, snake_y, 10, 10])
    pygame.display.update() #обновляем дисплей
    clock.tick(snake_speed) #скорость игры
display_message("Вы проиграли!!!", message_color) #Сообщение на экран
pygame.display.update() #обновляем дисплей
time.sleep(3)
pygame.quit()
#выходим из игры (закрытие окна при нажатии кнопки закрытия)
quit()