import pygame
import sys
from settings import *
from level import Level

class Button:
    def __init__(self, text, font, x, y, width, height, color1, color2):
        self.text = text
        self.font = font
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color1, self.rect)
        button_text_render = self.font.render(self.text, True, self.color2)
        button_text_x = self.rect.x + (self.rect.width - button_text_render.get_width()) // 2
        button_text_y = self.rect.y + (self.rect.height - button_text_render.get_height()) // 2
        screen.blit(button_text_render, (button_text_x, button_text_y))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Lobby:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_font = pygame.font.SysFont(None, 90)
        button_text = ["START", "LOAD", "QUIT"]
        button_y = HEIGHT // 2

        for text in button_text:
            button_render = button_font.render(text, True, color2)
            button_width, button_height = 200, 50
            button_x = (WIDTH - button_width) // 2
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            button = Button(text, button_font, button_x, button_y, button_width, button_height, color1, color2)
            self.buttons.append(button)
            button_y += button_height + 20

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                return self.handle_lobby_click(mouse_pos)

    def handle_lobby_click(self, mouse_pos):
        for button in self.buttons:
            if button.is_clicked(mouse_pos):
                if button.text == "START":
                    return "start"
                elif button.text == "LOAD":
                    return "load"
                elif button.text == "QUIT":
                    return "quit"

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_title()
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()

    def draw_title(self):
        title_font = pygame.font.SysFont(None, 64)
        title_text = "DREAM ADVENTURE"
        title_render = title_font.render(title_text, True, WHITE)
        title_x = (WIDTH - title_render.get_width()) // 2
        title_y = 100
        self.screen.blit(title_render, (title_x, title_y))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Dream Adventure')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.in_lobby = True
        self.lobby = Lobby(self.screen)

    def run(self):
        while True:
            if self.in_lobby:
                action = self.handle_lobby()
                if action == "start":
                    self.in_lobby = False
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill(BLACK)
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)

    def handle_lobby(self):
        while self.in_lobby:
            self.lobby.draw()
            action = self.lobby.handle_events()
            if action:
                return action


if __name__ == '__main__':
    pygame.mixer.music.load("/home/kyd/group13_project/music/back.mp3")
    pygame.mixer.music.play(-1)
    game = Game()
    game.run()

