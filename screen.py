import pygame

from snake import Snake
from defines import Directions

class Screen:
    def __init__(self, screen):
        self.screen = screen
        
class GameScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        
        self.snake = Snake()
        self.snake_dir = Directions.RIGHT
        self.img = pygame.image.load("assets/img/face.png").convert()
     
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
    
    def update(self):
        if self.snake_dir == Directions.RIGHT:
            self.snake.move(self.snake.position_x + 2, self.snake.position_y)
        elif self.snake_dir == Directions.LEFT:
            self.snake.move(self.snake.position_x - 2, self.snake.position_y)
        elif self.snake_dir == Directions.UP:
            self.snake.move(self.snake.position_x, self.snake.position_y - 2)
        elif self.snake_dir == Directions.DOWN:
            self.snake.move(self.snake.position_x, self.snake.position_y + 2)
    
    def render(self):
        self.screen.blit(self.img, (20,20))
        self.snake.render(self.screen)