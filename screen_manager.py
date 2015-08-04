import pygame
from pygame.locals import *

from screen import GameScreen

class ScreenManager:
    def __init__(self):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((640,480))
        self.continuer = True
        self.current_screen = GameScreen(self.screen)
        
    def run(self):
        while self.continuer:            
            
            self.event = pygame.event.wait()
            
            if self.event.type == pygame.QUIT:
                self.continuer = False
                
            self.current_screen.render()
            
            pygame.display.flip()