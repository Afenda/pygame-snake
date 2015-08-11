import pygame

from screen import Screen
from defines import Defines

class MenuScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        self.font = pygame.font.Font("assets/fonts/blogger-sans.ttf", 32)
        self.text = self.font.render("Pygame Snake", True, (0, 0, 0))
        self.fontbtn = pygame.font.Font("assets/fonts/blogger-sans.ttf", 22)
        self.textnew = self.fontbtn.render("New Game", True, (0, 0, 0))
        self.textload = self.fontbtn.render("Load", True, (0, 0, 0))
        self.textquit = self.fontbtn.render("Quit", True, (0, 0, 0))
        
    def manageEvents(self, event):
        if event.type == pygame.KEYDOWN:
            print("keyboard pressed")
            
    def update(self):
        return self
    
    def render(self):
        self.screen.fill(Defines.WHITE)
        self.screen.blit(self.textnew, (320 - self.textnew.get_width() // 2, 200))
        self.screen.blit(self.textload, (320 - self.textload.get_width() // 2, 250))
        self.screen.blit(self.textquit, (320 - self.textquit.get_width() // 2, 300))
        self.screen.blit(self.text, (320 - self.text.get_width() // 2, 20))