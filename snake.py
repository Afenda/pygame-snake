import pygame
from defines import Defines

class Snake:
    def __init__(self):
        self.inLife = True
        self.head_x = 200
        self.head_y = 200
        self.snake_coords = []
        self.snake_length = Defines.SNAKE_INIT_LENGTH
        for i in range(Defines.SNAKE_INIT_LENGTH):
            self.snake_coords.append([self.head_x - (20 * i), self.head_y])
        
    def move(self, x, y):
        if x > Defines.SCREEN_W - Defines.SNAKE_SIZE or x < 0 or y > Defines.SCREEN_H - Defines.SNAKE_SIZE or y < 0:
            self.inLife = False
        else:
            self.head_x = x
            self.head_y = y
            self.snake_coords.insert(0, [self.head_x, self.head_y])
            self.snake_coords.pop()
        
    def render(self, screen):
        for i in range(self.snake_length):
            pygame.draw.rect(screen, Defines.GREEN, [self.snake_coords[i][0], self.snake_coords[i][1], Defines.SNAKE_SIZE, Defines.SNAKE_SIZE])