import pygame

from screen import Screen
from defines import Defines

class MenuScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        
    def manageEvents(self, event):
        if event.type == pygame.KEYDOWN:
            print("keyboard pressed")
            
    def update(self):
        return self
    
    def render(self):
        self.screen.fill(Defines.PURPLE)