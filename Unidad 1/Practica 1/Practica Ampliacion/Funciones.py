import os

import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_p, K_n)

from BaseDatos import crear_conexion, recuperar_datos, insertar_datos
from Cloud import Cloud
from Constantes import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN, score, recur, screen, BLACK, BLUE, ADDENEMY, clock, \
    ROJITO, AZULITO, ADDCLOUD, FONDO_AZUL, collision_sound, RED, ADDHEART
from Enemy import Enemy
from Heart import Heart
from Player import Player


def inicio():
    hola = True
    score_font = pygame.font.SysFont(None, 60)
    score_font2 = pygame.font.SysFont(None, 40)
    while hola:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_p:
                    hola = False

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                pygame.quit()
                quit()
        conexion = crear_conexion("RegistroPuntuacion.db")
        avion = pygame.image.load(os.path.join(recur, "Avion_Fondo.jpg")).convert()
        screen.blit(avion, (0, 0))
        text = score_font.render("AIRPLANE VS MISSILES", True, ROJITO)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2.5))
        screen.blit(text, text_rect)
        text2 = score_font2.render("Pulsa P para empezar", True, AZULITO)
        text_rect2 = text2.get_rect()
        text_rect2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 1.5))
        screen.blit(text2, text_rect2)
        text3 = score_font2.render("High Score: " + str(recuperar_datos(conexion)), True, AZULITO)
        text_rect3 = text3.get_rect()
        screen.blit(text3, (SCREEN_WIDTH - text.get_width() - 10, text3.get_height() - 10))
        # Flip the display
        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


def final():
    hola = True
    score_font = pygame.font.SysFont(None, 60)
    score_font2 = pygame.font.SysFont(None, 40)
    while hola:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_n:
                    pygame.quit()
                    quit()

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                pygame.quit()
                quit()

        conexion = crear_conexion("RegistroPuntuacion.db")

        if score.score >= recuperar_datos(conexion):
            happy = pygame.transform.scale(pygame.image.load(os.path.join(recur, "happy.jpg")).convert(), (800, 600))
            screen.blit(happy, (0, 0))
            text0 = score_font2.render("FELICITACIONES HAS SUPERADO TU RECORD", True, BLACK)
            text_rect = text0.get_rect()
            text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 4.0))
            screen.blit(text0, text_rect)
            text2 = score_font2.render("High Score: " + str(recuperar_datos(conexion)), True, AZULITO)
            screen.blit(text2, (SCREEN_WIDTH - text2.get_width() - 10, text2.get_height() - 10))
            text3 = score_font2.render("Tu puntuacion: " + str(score.score), True, GREEN)
            text_rect = text3.get_rect()
            text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 1.2))
            screen.blit(text3, text_rect)
        else:
            sad = pygame.image.load(os.path.join(recur, "SAD.jpg")).convert()
            screen.blit(sad, (0, 0))
            text = score_font.render("GAME OVER", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2.5))
            screen.blit(text, text_rect)
            text3 = score_font2.render("Tu puntuacion: " + str(score.score), True, GREEN)
            text_rect = text3.get_rect()
            text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 1.5))
            screen.blit(text3, text_rect)
            text2 = score_font2.render("High Score: " + str(recuperar_datos(conexion)), True, AZULITO)
            screen.blit(text2, (SCREEN_WIDTH - text2.get_width() - 10, text2.get_height() - 10))
        # Flip the display
        pygame.display.flip()
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)


def jugar():
    player = Player()
    player_health = 200
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    corazones = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    dianoche = True
    color_fondo = BLUE
    u_vc = 0
    running = True
    while running:
        vc = int(50 + (450 / score.level))
        if u_vc != vc:
            u_vc = vc
            pygame.time.set_timer(ADDENEMY, vc)

        # Did the user click the window close button?
        for event in pygame.event.get():

            # Did the user hit a key?
            if event.type == KEYDOWN:

                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                running = False

            # Add a new enemy?
            elif event.type == ADDENEMY:

                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            # Add a new cloud?
            elif event.type == ADDCLOUD:

                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

            # Alternate between day and night
            elif event.type == FONDO_AZUL:
                if dianoche:
                    color_fondo = (BLACK)
                    dianoche = False
                else:
                    color_fondo = (BLUE)
                    dianoche = True

            elif event.type == ADDHEART:
                new_heart = Heart()
                corazones.add(new_heart)
                all_sprites.add(new_heart)

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Update enemy position
        enemies.update(score)

        # Update cloud position
        clouds.update()

        # Update hearts
        corazones.update()

        # Fill the screen with black
        screen.fill(color_fondo)

        text = score.score_font.render("Score: " + str(score.score), True, RED)
        text3 = score.score_font.render("Level: " + str(score.level), True, RED)
        screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, text.get_height() - 10))
        screen.blit(text3, (SCREEN_WIDTH - text.get_width() - 400, text.get_height() - 10))

        pygame.draw.rect(screen, RED, (1, 1, 200, 15))
        pygame.draw.rect(screen, GREEN, (1, 1, player_health, 15))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollide(player, enemies, True):
            if player_health > 50:
                player_health -= 50
            else:
                # If so, then remove the player and stop the loop
                collision_sound.play()
                insertar_datos()
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                player.kill()
                final()
                running = False

        if pygame.sprite.spritecollide(player, corazones, True):
            if player_health < 200:
                player_health += 50

        # Draw the player on the screen
        # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(player.surf, player.rect)

        # Flip the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
