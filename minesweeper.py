import sys
import os
import random
import pygame

pygame.init()


# CONSTANTS


WIDTH, HEIGHT = 255, 255
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

FIELD_S = 10

BOX_MES = 20
MARGIN = 5

WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREY = [128, 128, 128]

FLAG = pygame.image.load(os.path.join('assets', 'img', 'flag.png'))

# create 2d array of 0s
grid = []
for row in range(FIELD_S):
    grid.append([])
    for column in range(FIELD_S):
        grid[row].append(0)


# FUNCTIONS


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        for row in range(FIELD_S):
            for column in range(FIELD_S):
                color = WHITE
                pygame.draw.rect(screen, color, [(MARGIN + BOX_MES) * column + MARGIN, (MARGIN + BOX_MES) * row + MARGIN, BOX_MES, BOX_MES])

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit("End of the line, bucko")


# INITIALIZE


if __name__ == '__main__':
    main()
