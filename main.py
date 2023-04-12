import pygame,sys
from setting import *
from level import Level

class Game:
  def __init__(self):
    
    # initial setting
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
    pygame.display.set_caption('交大歷險記')
    self.clock  = pygame.time.Clock()
    
    self.level = Level()
  def run(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.fill((0,0,0))
        self.level.run()
        pygame.display.update()
        self.clock.tick(FPS)
if __name__ == '__main__':
  game = Game()
  game.run()
