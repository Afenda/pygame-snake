class Screen:
    def __init__(self, screen):
        self.screen = screen
    
    def manageEvents(self, event):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def render(self):
        raise NotImplementedError