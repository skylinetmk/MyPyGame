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

#пока игра продолжается
while not game_over:
   for event in pygame.event.get():
       print(event)  #Выводить в терминал все произошедшие события.
       if event.type==pygame.QUIT:
           game_over=True


#разинициализируем pygame
pygame.quit()
#выходим из игры (закрытие окна при нажатии кнопки закрытия)
quit()