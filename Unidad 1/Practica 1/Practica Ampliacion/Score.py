import pygame


class Score:
    def __init__(self):
        self.score = 0
        self.contador = 1
        self.hscore = 0
        self.level = 1
        self.score_font = pygame.font.SysFont(None, 30)
        self.text = ""
        self.text2 = ""
        self.text3 = ""
