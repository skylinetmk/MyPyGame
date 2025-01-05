import pygame
#from sprites import ground_height
# размеры падающих животных
animal_width = 40
animal_height = 40

# класс переписана функция инициализации, позволяет определить поверхность и rect
class Animals(pygame.sprite.Sprite):
    # параметры падающих животных

    def __init__(self, x, speed, surf, group):

        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0),width=animal_width,height=animal_height)
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - animal_height - args[1]:
            self.rect.y += self.speed
        else:
            self.kill()
