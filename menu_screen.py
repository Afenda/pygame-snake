import sys,pygame

from screen import Screen
from game_screen import GameScreen
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
        self.choice = 0
        
    def manageEvents(self, event):
        if event.type == pygame.MOUSEMOTION:
            posX = event.pos[0]
            posY = event.pos[1]
            
            self.textnew = self.fontbtn.render("New Game", True, (0, 0, 0))
            self.textload = self.fontbtn.render("Load", True, (0, 0, 0))
            self.textquit = self.fontbtn.render("Quit", True, (0, 0, 0))
            
            if(
                posX >= (320 - self.textnew.get_width()//2) and
                posX <= ((320 - self.textnew.get_width()//2)+self.textnew.get_width()) and
                posY >= 200 and
                posY <= 200 + self.textnew.get_height()
                ):
                self.textnew = self.fontbtn.render("New Game", True, (255, 0, 0))
            if(
                posX >= (320 - self.textload.get_width()//2) and
                posX <= ((320 - self.textload.get_width()//2)+self.textload.get_width()) and
                posY >= 250 and
                posY <= 250 + self.textload.get_height()
                ):
                self.textload = self.fontbtn.render("Load", True, (255, 0, 0))
            if(
                posX >= (320 - self.textquit.get_width()//2) and
                posX <= ((320 - self.textquit.get_width()//2)+self.textquit.get_width()) and
                posY >= 300 and
                posY <= 300 + self.textquit.get_height()
                ):
                self.textquit = self.fontbtn.render("Quit", True, (255, 0, 0))                
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX = event.pos[0]
            posY = event.pos[1]
            if(
                posX >= (320 - self.textnew.get_width()//2) and
                posX <= ((320 - self.textnew.get_width()//2)+self.textnew.get_width()) and
                posY >= 200 and
                posY <= 200 + self.textnew.get_height()
                ):
                self.choice = 1
            elif(
                posX >= (320 - self.textload.get_width()//2) and
                posX <= ((320 - self.textload.get_width()//2)+self.textload.get_width()) and
                posY >= 250 and
                posY <= 250 + self.textload.get_height()
                ):
                self.choice = 2
            if(
                posX >= (320 - self.textquit.get_width()//2) and
                posX <= ((320 - self.textquit.get_width()//2)+self.textquit.get_width()) and
                posY >= 300 and
                posY <= 300 + self.textquit.get_height()
                ):
                self.choice = 3 
              
    def update(self):
        if self.choice != 0:
            if self.choice == 1:
                return GameScreen(self.screen)
            elif self.choice == 2:
                return self
            elif self.choice == 3:
                sys.exit()
        else:
            return self
    
    def render(self):
        self.screen.fill(Defines.WHITE)
        self.screen.blit(self.textnew, (320 - self.textnew.get_width() // 2, 200))
        self.screen.blit(self.textload, (320 - self.textload.get_width() // 2, 250))
        self.screen.blit(self.textquit, (320 - self.textquit.get_width() // 2, 300))
        self.screen.blit(self.text, (320 - self.text.get_width() // 2, 20))