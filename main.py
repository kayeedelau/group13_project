import pygame, sys, button
from settings import *
from level import Level
from player import Player
class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Dream Adventure')
		
		self.clock = pygame.time.Clock()
		self.level = Level([('Skin', '1'), ('score', '500'), ('health', '50'), ('energy', '50'), ('pos', '(4736,128)'), ('speed', '5')]
)
		
	def save_game_data(self,ID,skin):
	
		score  =self.level.get_exp()
		health =self.level.get_health()
		energy =self.level.get_energy()
		pos    =self.level.get_pos().topleft
		speed  =self.level.get_speed()
	
		file_name = f'{ID}.txt'
		with open(file_name, 'w')as file:
			file.write(f'Skin:{skin}\n')
			file.write(f'score:{score}\n')
			file.write(f'health:{health}\n')
			file.write(f'energy:{energy}\n')
			file.write(f'pos:{pos}\n')
			file.write(f'speed:{speed}\n')
	
	def load_game_save(self,ID):
		player=[]
		with open(f'{ID}.txt','r') as file:
			for line in file:
				key, value = line.strip().split(':')
				player.append((key,value))
		return player
		
	def run(self):
		run = False
		lobby = True
		setting = False
		loading =False
		# menu setting
		game_paused = False
		menu_state= 'main'
		
		font = pygame.font.SysFont('Arial',100)
		text = font.render('Dream Adventure',True,(255,255,255))
		text_rect = text.get_rect(center=(WIDTH//2,70))
		text1= font.render('Input your ID:',True,(255,255,255))
		text1_rect = text.get_rect(center=(WIDTH/2,HEIGHT//3))
		# pause control
		self.is_time_stopped = False
		
		# click sfx
		sfx = pygame.mixer.Sound('./audio/click.mp3')
		
		# image loading
		start_img   = pygame.image.load('./graphics/start.png').convert_alpha()
		load_img	= pygame.image.load('./graphics/load.png').convert_alpha()
		quit_img	= pygame.image.load('./graphics/quit.png').convert_alpha()
		
		#create button instances
		start_button   = button.Button(WIDTH//2, HEIGHT//7*2, start_img, 1)
		load_button	= button.Button(WIDTH//2, HEIGHT//7*4, load_img, 1)
		quit_button	= button.Button(WIDTH//2, HEIGHT//7*6, quit_img, 1)

		number = ""
		game = True
		font1 = pygame.font.Font(None, 36)
		input_rect = pygame.Rect(WIDTH//2, HEIGHT//2, 200, 40)
		input_active = True
		
		while game:
			while lobby:
				self.screen.fill(BLACK)
				self.screen.blit(text,text_rect)
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
						
				if start_button.draw(self.screen):
					sfx.play()
					pygame.time.delay(500)
					lobby =False
					run = False
					setting = True
					self.save_game_data(number,1)
					
				if load_button.draw(self.screen):
					sfx.play()
					pygame.time.delay(500)
					lobby =False
					run = False
					loading=True
					
					
				if quit_button.draw(self.screen):
					sfx.play()
					pygame.time.delay(700)
					lobby= False
					run=False
					game = False
				pygame.display.update()
			while loading:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								run = True
								loading = False
								file_name = self.load_game_save(number)
								self.level= Level(file_name)
							elif event.key == pygame.K_BACKSPACE:
								# Remove the last character
								number = number[:-1]
							elif event.unicode.isnumeric():
								# Append the numeric character to the number
								number += event.unicode
			
				# Render the screen
				self.screen.fill((0, 0, 0))
				self.screen.blit(text1,text1_rect)
				pygame.draw.rect(self.screen, WHITE, input_rect, 2)
				input_text = font1.render(number, True, WHITE)
				self.screen.blit(input_text, (input_rect.x + 5, input_rect.y + 5))
				pygame.display.flip()
				
			while setting:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								setting = False
								run = True
							elif event.key == pygame.K_BACKSPACE:
								# Remove the last character
								number = number[:-1]
							elif event.unicode.isnumeric():
								# Append the numeric character to the number
								number += event.unicode
			
				# Render the screen
				self.screen.fill((0, 0, 0))
				self.screen.blit(text1,text1_rect)
				pygame.draw.rect(self.screen, WHITE, input_rect, 2)
				input_text = font1.render(number, True, WHITE)
				self.screen.blit(input_text, (input_rect.x + 5, input_rect.y + 5))
				pygame.display.flip()
	
			# image loading
			resume_img  = pygame.image.load('./graphics/resume.png').convert_alpha()
			options_img = pygame.image.load('./graphics/option.png').convert_alpha()
			quit_img	= pygame.image.load('./graphics/quit.png').convert_alpha()
			audio_img   = pygame.image.load('./graphics/audio.png').convert_alpha()
			audio_gray  = pygame.image.load('./graphics/audio_gray.png').convert_alpha()
			back_img	= pygame.image.load('./graphics/back.png').convert_alpha()
			
			#create button instances
			resume_button  = button.Button(WIDTH//2, HEIGHT//7*2, resume_img, 1)
			quit_button	= button.Button(WIDTH//2, HEIGHT//7*6, quit_img, 1)
			audio_normal   = button.Button(WIDTH//2, HEIGHT//7*4, audio_img, 1)
			audio_gray	 = button.Button(WIDTH//2, HEIGHT//7*4, audio_gray, 1)
			
			# audio control
			self.is_mute = False
			
			# sound 
			main_sound = pygame.mixer.Sound('./audio/main.ogg')
			main_sound.set_volume(0.5)
			main_sound.play(loops = -1)
				
			while run:
				if not self.is_mute:
					main_sound.set_volume(0.5)
					audio_button = audio_normal
				else:
					main_sound.set_volume(0)
					audio_button = audio_gray
					
				self.screen.fill(BLACK)
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_p:
							game_paused = True
				
				if game_paused:
					self.is_time_stopped = True
					if menu_state == "main":
						if resume_button.draw(self.screen):
							sfx.play()
							pygame.time.delay(500)
							game_paused = False
							self.is_time_stopped = False
						if audio_button.draw(self.screen):
							sfx.play()
							pygame.time.delay(500)
							self.is_mute = not self.is_mute
						if quit_button.draw(self.screen):
							sfx.play()
							pygame.time.delay(500)
							run = False
							lobby = True
							self.save_game_data(number,1)
				if not self.is_time_stopped:
					self.level.run()
				pygame.display.update()
				self.clock.tick(FPS)
				
if __name__ == '__main__':
	game = Game()
	game.run()
