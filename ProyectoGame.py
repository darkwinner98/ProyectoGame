# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:31:30 2024

@author: darwi
"""

import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi Juego con PyGame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Fuente
font = pygame.font.Font(None, 74)

# Funciones personalizadas
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Mi Juego", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Presiona una tecla para comenzar", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_loop()

        pygame.display.update()
        clock.tick(FPS)

def game_loop():
    player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)
    enemies = [pygame.Rect(random.randint(0, WIDTH-50), random.randint(-1000, -50), 50, 50) for _ in range(5)]
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        screen.fill(WHITE)

        # Dibujar jugador
        pygame.draw.rect(screen, BLACK, player)

        # Dibujar enemigos
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)
            enemy.y += 5
            if enemy.top > HEIGHT:
                enemy.x = random.randint(0, WIDTH-50)
                enemy.y = random.randint(-1000, -50)
                score += 1

        # Mostrar puntuación
        draw_text(f'Score: {score}', font, BLACK, screen, WIDTH // 2, 50)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()
