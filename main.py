import pygame
from pygame.locals import *
from snake import *

pygame.init()
screen = pygame.display.set_mode((640,480))

print("Hello World");

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0