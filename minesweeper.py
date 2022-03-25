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

WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREY = [128, 128, 128]

FLAG = pygame.image.load(os.path.join('assets', 'img', 'flag.png'))


# FUNCTIONS


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit("Reached end of sequence")


# INITIALIZE


if __name__ == '__main__':
    main()
