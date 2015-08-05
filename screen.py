import pygame

from snake import Snake
from defines import *

class Screen:
    def __init__(self, screen):
        self.screen = screen
        
class GameScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        
        self.snake = Snake()
        self.snake_dir = Directions.RIGHT
        self.inPause = False
        self.pauseImg = pygame.image.load('assets/img/pause.png').convert();
        self.pauseImg.set_colorkey(Defines.COLORKEY)
     
    def manageEvents(self, event):
        #For testing Keyboard use event.dict['unicode'] because in default keyboard type is in American
        if event.type == pygame.KEYDOWN:
            if event.dict['unicode'] == "z" or event.key == pygame.K_UP:
                self.snake_dir = Directions.UP
            elif event.dict['unicode'] == "s" or event.key == pygame.K_DOWN:
                self.snake_dir = Directions.DOWN
            elif event.dict['unicode'] == "q" or event.key == pygame.K_LEFT:
                self.snake_dir = Directions.LEFT
            elif event.dict['unicode'] == "d" or event.key == pygame.K_RIGHT:
                self.snake_dir = Directions.RIGHT
            elif event.key == pygame.K_SPACE:
                self.inPause = False if self.inPause else True 
    
    def update(self):
        if self.snake.inLife:
            if not self.inPause:
                if self.snake_dir == Directions.RIGHT:
                    self.snake.move(self.snake.head_x + Defines.SNAKE_SIZE + 1, self.snake.head_y)
                elif self.snake_dir == Directions.LEFT:
                    self.snake.move(self.snake.head_x - Defines.SNAKE_SIZE - 1, self.snake.head_y)
                elif self.snake_dir == Directions.UP:
                    self.snake.move(self.snake.head_x, self.snake.head_y - Defines.SNAKE_SIZE - 1)
                elif self.snake_dir == Directions.DOWN:
                    self.snake.move(self.snake.head_x, self.snake.head_y + Defines.SNAKE_SIZE + 1)
    
    def render(self):
        self.snake.render(self.screen)
        if not self.snake.inLife:
            imgDie = pygame.Surface((640,480))
            imgDie.set_alpha(128)
            imgDie.fill((255, 0, 0))
            self.screen.blit(imgDie, (0, 0))
            
        if self.inPause:
            self.screen.blit(self.pauseImg, (195, 215))