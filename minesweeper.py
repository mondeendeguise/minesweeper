import numpy as np
import pygame
import random
import os
import sys


# FUNCTIONS


def game():
    pygame.init()

    WIDTH, HEIGHT = 500, 500
    FPS = 15

    TILES = 25
    SIZE = 20
    MARGIN = 5

    WHITE = [255, 255, 255]
    RED = [255, 0, 0]
    GREY = [128, 128, 128]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    grid = np.zeros((TILES, TILES), dtype=int)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("User closed window")
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = []
                clicked.append(pygame.mouse.get_pos()[1] // TILES)
                clicked.append(pygame.mouse.get_pos()[0] // TILES)
                print(clicked)
                grid[clicked[0], clicked[1]] = 1
        # draw grid
        for row in range(TILES):
            for column in range(TILES):
                if grid[row, column] == 0:
                    color = WHITE
                elif grid[row, column] == 1:
                    color = GREY
                pygame.draw.rect(screen, color, [(MARGIN + SIZE) * column + MARGIN, (MARGIN + SIZE) * row + MARGIN, SIZE, SIZE])
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit("Reached end of sequence")


# INITIALIZE


if __name__ == '__main__':
    game()
