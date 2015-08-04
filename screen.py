import pygame

class Screen:
    def __init__(self, screen):
        self.screen = screen
        
class GameScreen(Screen):
    
    def __init__(self, screen):
        Screen.__init__(self, screen)
        self.img = pygame.image.load("assets/img/face.png").convert()
        
    def render(self):
        self.screen.blit(self.img, (20,20))