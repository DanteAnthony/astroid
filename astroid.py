import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

# screen size
screen_width = 936
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Astroid')

bg = pygame.image.load("astroid/img/spacebg.png")

# game run
run = True
while run:

    clock.tick(fps)

    screen.blit(bg, (0, 0))

    # stop / start game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()