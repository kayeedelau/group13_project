import pygame,sys
from settings import *
from level import Level

class Game:
    def __init__(self):
    
    # initial setting
      pygame.init()
      self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
      pygame.display.set_caption('交大歷險記')
      self.clock  = pygame.time.Clock()
      self.level = Level()
      self.in_lobby = True
    
    
    def lobby(self):
        while self.in_lobby:
            self.handle_events()
            self.draw_lobby()
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.in_lobby:
                    self.handle_lobby_click(mouse_pos)

    def handle_lobby_click(self, mouse_pos):
        if self.start_button_rect.collidepoint(mouse_pos):
            self.in_lobby = False

    def draw_lobby(self):
        self.screen.fill(BLACK)
        self.draw_title()
        self.draw_start_button()

    def draw_title(self):
        title_font = pygame.font.SysFont(None, 64)
        title_text = "游戏大厅"
        title_render = title_font.render(title_text, True, WHITE)
        title_x = (WIDTH - title_render.get_width()) // 2
        title_y = 100
        self.screen.blit(title_render, (title_x, title_y))

    def draw_start_button(self):
        button_font = pygame.font.SysFont(None, 90)
        button_text = "START"
        self.start_button_rect = self.draw_button(button_font, button_text, HEIGHT // 2,color1 )

    def draw_button(self, font, text, y, color1):
        button_render = font.render(text, True, color2)
        button_width, button_height = 200, 50
        button_x = (WIDTH - button_width) // 2
        button_y = y
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(self.screen, color1, button_rect)
        button_text_x = button_x + (button_width - button_render.get_width()) // 2
        button_text_y = button_y + (button_height - button_render.get_height()) // 2
        self.screen.blit(button_render, (button_text_x, button_text_y))
        return button_rect

    def run(self):
        while True:
            self.handle_events()
            self.screen.fill(BLACK)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def quit_game(self):
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
  game = Game()
  game.lobby()
  game.run()
