import pygame
import sys #lets you mess w runtime environment & variables/functions that interact with the interpreter
from settings import * #lets you access config/settings properties from all python modules
from level import Level 

# ------- CLASS GAME -------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True: # --- GAME LOOP ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() # exits interpreter

            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update() #like flip but different
        
if __name__=='__main__':
    game = Game()
    game.run() # keeps the game safe by making it run away from danger