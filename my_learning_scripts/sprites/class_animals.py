import pygame

# класс переписана функция инициализации, позволяет определить поверхность и rect
class Animals(pygame.sprite.Sprite):

    # параметры падающих животных
    def __init__(self, width, height, x, speed, score, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0),width=width,height=height)
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - self.height - args[1]:
            self.rect.y += self.speed
        else:
            self.kill()





