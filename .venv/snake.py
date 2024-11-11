import pygame
#инициализируем pygame
pygame.init()
#создаем окно с игрой - дисплей
dis = pygame.display.set_mode((500, 400))  # Задаём размер игрового поля.
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

snake_x = 300 #Указываем начальное значение положения змейки по оси х.
snake_y = 300 #Указываем начальное значение положения змейки по оси y.
snake_x_change = 0 #Создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси х.
snake_y_change = 0 #создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки по оси y.
clock = pygame.time.Clock() # для использования игрового времени (скорости игры)




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
    snake_x += snake_x_change #Записываем новое значение положения змейки по оси х.
    snake_y += snake_y_change #Записываем новое значение положения змейки по оси y.
    dis.fill(white)

    pygame.draw.rect(dis, black, [snake_x, snake_y, 10, 10])
    pygame.display.update() #обновляем дисплей
    clock.tick(30) #скорость игры

#разинициализируем pygame
pygame.quit()
#выходим из игры (закрытие окна при нажатии кнопки закрытия)
quit()