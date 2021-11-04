import os
import random

import pygame
from pygame import RLEACCEL

from Constantes import recur, SCREEN_WIDTH, SCREEN_HEIGHT, score


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.vc = 0
        self.ve = 0
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(recur, "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2 * score.level, 10 + 3 * score.level)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, score):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            score.score += 10
        if score.score > score.hscore:
            score.hscore = score.score

        if score.score - (500 * score.contador) == 0:
            score.level += 1
            score.score += 10
            score.contador += 1