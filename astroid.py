import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

# screen set up
screen_width = 936
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Astroid')

bg = pygame.image.load("astroid/img/spacebg.png")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("astroid/img/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        pass

player_group = pygame.sprite.Group()
player = Player(int(screen_width / 2), int(screen_height / 2))
player_group.add(player)

# game run
run = True
while run:

    clock.tick(fps)

    screen.blit(bg, (0, 0))

    player_group.draw(screen)

    # stop / start game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()