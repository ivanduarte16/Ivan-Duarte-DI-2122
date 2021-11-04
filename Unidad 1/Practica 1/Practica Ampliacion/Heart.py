import os
import random

import pygame
from pygame import RLEACCEL

from Constantes import recur, SCREEN_WIDTH, SCREEN_HEIGHT


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super(Heart, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load(os.path.join(recur, "corazon.png")).convert(), (40, 40))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = -5

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()