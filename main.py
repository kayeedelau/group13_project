import pygame
import sys
import json
from settings import *
from level import Level

class GameSave:
	def __init__(self, player_id):
		self.player_id = player_id
		self.filename = f"{player_id}.json"
		
	def save_game(self, skin , health, mana, position):
		game_data ={
			"player_id": self.player_id,
			"skin": skin,
			"health": health,
			"mana": mana,
			"position": position
		}
		with open(self.filename, 'w') as file:
			json.dump(game_data, file)
	def load_game(self):
		with open(self.filename, "r") as file:
			game_data = json.load(file)
		return game_data["skin"],game_data["health"],game_data["mana"],game_data["position"]

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
					return self.handle_load_button()
				elif button.text == "QUIT":
					return "quit"
					
	def handle_load_button(self):
		pygame.draw.rect(self.screen, BLACK, (0,0,WIDTH, HEIGHT))
		font = pygame.font.SysFont(None, 60)
		text_surface = font.render("Enter Player ID:", True, WHITE)
		text_rect = text_surface.get_rect(center=(WIDTH //2, HEIGHT//2))
		input_rect = pygame.Rect(text_rect.x, text_rect.y + 100, text_rect.width, 40)
		input_active = True
		player_id = ""
		
		while input_active:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						input_active = False
					elif event.key == pygame.K_BACKSPACE:
						player_id = player_id[:-1]
					else:
						player_id += event.unicode

			pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT))
			pygame.draw.rect(self.screen, WHITE, input_rect, 2)
			self.screen.blit(text_surface, text_rect)
			font_input = pygame.font.SysFont(None, 40)
			input_surface = font_input.render(player_id, True, WHITE)
			self.screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
			input_rect.w = max(200, input_surface.get_width() + 10)
			pygame.display.flip()

		return "load", player_id

		
	def draw(self):
		self.screen.fill(BLACK)
		self.draw_title()
		for button in self.buttons:
			button.draw(self.screen)
		pygame.display.update()

	def draw_title(self):
		title_font = pygame.font.SysFont(None, 100)
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
		
		# sound
		#main_sound = pygame.mixer.Sound('path')
		#main_sound.set_volume(0.5)
		#main_sound.play(loops = -1)

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
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_m:										self.level.toggle_menu()
				self.screen.fill(WATER_COLOR)
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
	pygame.mixer.music.load("/home/kelvinyeh/group13_project/music/back.mp3")
	pygame.mixer.music.play(-1)
	game = Game()
	game.run()

