import sys, pygame
from pygame.locals import *

from game_screen import GameScreen
from menu_screen import MenuScreen
from defines import Defines

class ScreenManager:
    def __init__(self):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption('Pygame - Snake')
        #self.current_screen = GameScreen(self.screen)
        self.current_screen = MenuScreen(self.screen)
        self.clock = pygame.time.Clock()
        
    def run(self):
        
        while 1:            
            new_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.current_screen.manageEvents(event)
                    
            self.current_screen = self.current_screen.update()
            
            #clear screen
            self.screen.fill(Defines.BLUE)
            
            self.current_screen.render()
            
            pygame.display.flip()
            self.clock.tick(5)