import pygame

class Game:
    def __init__(self, width, height, fps=60):
        self.width = width
        self.height = height
        self.screen_rect = pygame.Surface((width, height))
        self.screen = pygame.display.set_mode((width, height))
        
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
    
    def event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            
    
    def tick(self):
        pass
    
    def update(self):
        self.screen.fill((255, 255, 255))
        pygame.display.update()
    
    def run(self):
        while self.running:
            self.event()
            self.tick()
            self.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game(800, 600)
    game.run()
