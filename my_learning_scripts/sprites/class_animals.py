import pygame


# класс переписана функция инициализации, позволяет определить поверхность и rect
class Animals(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0), width=40, height=40)
        self.speed = speed

    def update(self, *args):
        if self.rect.y < args[0] - self.rect.height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0