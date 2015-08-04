import pygame
from defines import Defines

class Snake:
    def __init__(self):
        self.inLife = True
        self.position_x = 200
        self.position_y = 200
        
    def move(self, x, y):
        self.position_x = x
        self.position_y = y
        
    def render(self, screen):
        pygame.draw.rect(screen, Defines.GREEN, [self.position_x, self.position_y, Defines.SNAKE_SIZE, Defines.SNAKE_SIZE])