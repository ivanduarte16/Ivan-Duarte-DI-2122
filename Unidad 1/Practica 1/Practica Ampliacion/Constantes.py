import os

import pygame

from Score import Score

direc = os.path.dirname(__file__)
recur = os.path.join(direc, "resources")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GREEN = (10, 74, 27)
BLUE = (97, 175, 219)
BLACK = (10, 10, 10)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 12)
ROJITO = (133, 44, 0)
AZULITO = (7, 142, 128)
BLANCO = (255, 255, 255)
ROSA = (90, 21, 97)

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

FONDO_AZUL = pygame.USEREVENT + 3
pygame.time.set_timer(FONDO_AZUL, 20000)

FONDO_INICIO = pygame.USEREVENT + 4
pygame.time.set_timer(FONDO_INICIO, 80000)

ADDHEART = pygame.USEREVENT + 5
pygame.time.set_timer(ADDHEART, 30000)

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Instantiate score.
score = Score()

# Load and play background music
pygame.mixer.music.load(os.path.join(recur, "ACD.ogg"))
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound(os.path.join(recur, "Rising_putter.ogg"))

move_down_sound = pygame.mixer.Sound(os.path.join(recur, "Falling_putter.ogg"))

# Run until the user asks to quit

collision_sound = pygame.mixer.Sound(os.path.join(recur, "Collision.ogg"))