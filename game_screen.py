import pygame

from random import randint

from snake import Snake
from screen import Screen
from defines import *

class GameScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        
        self.snake = Snake()
        self.snake_dir = Directions.RIGHT
        self.inPause = False
        self.pauseImg = pygame.image.load('assets/img/pause.png').convert();
        self.pauseImg.set_colorkey(Defines.COLORKEY)
        self.apple = (20,20)
        self.score = 0;
        self.font = pygame.font.Font("assets/fonts/blogger-sans.ttf", 24)
        self.fontL = pygame.font.Font("assets/fonts/blogger-sans.ttf", 48)
        self.scoretxt = self.font.render("score %d" % self.score, True, (0, 0, 0))
        self.txtloose = self.fontL.render("You Loose", True, (0, 0, 0))
        
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
                    
                if self.snake.head_x == self.apple[0] and self.snake.head_y == self.apple[1]:
                    self.score += 10
                    self.scoretxt = self.font.render("score %d" % self.score, True, (0, 0, 0))
                    self.apple = (randint(0, 31) * 20, randint(0, 23) * 20)
                    self.snake.snake_length = self.snake.snake_length + 1
                    self.snake.snake_coords.insert(0, [self.snake.head_x, self.snake.head_y])
                    
        return self
                    
    def render(self):
        self.snake.render(self.screen)
        if not self.snake.inLife:
            imgDie = pygame.Surface((640,480))
            imgDie.set_alpha(128)
            imgDie.fill((255, 0, 0))
            self.screen.blit(imgDie, (0, 0))
            self.screen.blit(self.txtloose, (320 - self.txtloose.get_width() // 2,200))

        self.screen.blit(self.scoretxt, (10, 5))

        pygame.draw.rect(self.screen, Defines.RED, [self.apple[0], self.apple[1], Defines.SNAKE_SIZE, Defines.SNAKE_SIZE])
            
        if self.inPause:
            self.screen.blit(self.pauseImg, (195, 215))