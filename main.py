import pygame, sys, button
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Dream Adventure')
		
		self.clock = pygame.time.Clock()
		self.level = Level()
		
		
	def draw_text(text, font, text_col, x, y):
		img = font.render(text,True, text_col)
		screen.blit(img, (x,y))
	
	
	def run(self):
		run = True
		# menu setting
		game_paused = False
		menu_state= 'main'
		
		font = pygame.font.SysFont('arialblack',40)
		TEXT_COL = (255,255,255)
		
		# image loading
		resume_img  = pygame.image.load('./graphics/resume.png').convert_alpha()
		options_img = pygame.image.load('./graphics/option.png').convert_alpha()
		quit_img    = pygame.image.load('./graphics/quit.png').convert_alpha()
		load_img    = pygame.image.load('./graphics/load.png').convert_alpha()
		audio_img   = pygame.image.load('./graphics/audio.png').convert_alpha()
		audio_gray  = pygame.image.load('./graphics/audio_gray.png').convert_alpha()
		start_img   = pygame.image.load('./graphics/start.png').convert_alpha()
		back_img    = pygame.image.load('./graphics/back.png').convert_alpha()
		
		#create button instances
		resume_button  = button.Button(WIDTH//2, HEIGHT//7*1.5, resume_img, 1)
		option_button  = button.Button(WIDTH//2, HEIGHT//7*3, options_img, 1)
		quit_button    = button.Button(WIDTH//2, HEIGHT//7*4.5, quit_img, 1)
		load_button    = button.Button(WIDTH//2, HEIGHT//7, load_img, 1)
		audio_normal   = button.Button(WIDTH//2, HEIGHT//7*3, audio_img, 1)
		audio_gray     = button.Button(WIDTH//2, HEIGHT//7*3, audio_gray, 1)
		start_button   = button.Button(WIDTH//2, 325, start_img, 1)
		back_button    = button.Button(WIDTH//2, HEIGHT//7*4.5, back_img, 1)
		
		# sound 
		main_sound = pygame.mixer.Sound('./audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
		# pause control
		self.is_time_stopped = False
		
		# audio control
		self.is_mute = False
		
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
						game_paused = False
						self.is_time_stopped = False
					if audio_button.draw(self.screen):
						self.is_mute = not self.is_mute
					if quit_button.draw(self.screen):
						run = False
			if not self.is_time_stopped:
				self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			
if __name__ == '__main__':
	game = Game()
	game.run()
