import pygame, sys, button, cv2
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
		self.level = Level([['Skin', '1'], ('score', '500'), ('health', '50'), ('energy', '50'), ('pos', '(4736,128)'), ('speed', '5')])
		self.is_dead = False
		
	def save_game_data(self,ID):
		skin   =self.level.player_data[0][1]
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
			
	def death_check(self):
		health = self.level.get_health()
		if health <=0:
			self.is_dead =True

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
		game = True
		skin_sel = False
		can_switch_skin = True
		confirm = False
		skin_index =1	
		skin_cooldown=400
		
		# menu setting
		game_paused = False
		menu_state= 'main'
		
		menu = pygame.image.load('./graphics/menu.png')
		menu = pygame.transform.scale(menu,(400,125))
		background = pygame.image.load('./cool/floor.png')
		font = pygame.font.SysFont('Arial',50)
		title = pygame.image.load('./graphics/Dream Adventure.png')
		title = pygame.transform.scale(title,(720,240))
		text1= font.render('Set your ID:',True,(255,255,255))
		text2= font.render('Input your ID:',True,(255,255,255))
		text1_rect = text1.get_rect(center=(400,400))
		text3= font.render('Choose your character:',True,(255,255,255))
		text4= font.render('Press Space to Confirm',True,(150,150,150))
		
		# pause control
		self.is_time_stopped = False
		
		# click sfx
		sfx = pygame.mixer.Sound('./audio/click.mp3')
		
		# image loading
		start_img   = pygame.image.load('./graphics/start.png').convert_alpha()
		load_img	= pygame.image.load('./graphics/load.png').convert_alpha()
		quit_img	= pygame.image.load('./graphics/quit.png').convert_alpha()
		start_img   = pygame.transform.scale(start_img,(400,125))
		load_img    = pygame.transform.scale(load_img,(400,125))
		quit_img    = pygame.transform.scale(quit_img,(400,125))
		
		#create button instances
		start_button   = button.Button(WIDTH//2, HEIGHT//7*3, start_img, 1)
		load_button	= button.Button(WIDTH//2, HEIGHT//7*4.5, load_img, 1)
		quit_button	= button.Button(WIDTH//2, HEIGHT//7*6, quit_img, 1)

		number = ""
		font1 = pygame.font.Font(None, 70)
		input_rect = pygame.Rect(WIDTH//2-50, HEIGHT//2-20, 200, 48)
		
		while game:
			while lobby:
				self.screen.fill(BLACK)
				self.screen.blit(background,(0,0))
				self.screen.blit(title,(280,0))
		
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
					self.save_game_data(number)
					
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
				self.screen.blit(background,(0,0))
				self.screen.blit(text2,text1_rect)
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
								skin_sel = True
								run= False
							elif event.key == pygame.K_BACKSPACE:
								# Remove the last character
								number = number[:-1]
							elif event.unicode.isnumeric():
								# Append the numeric character to the number
								number += event.unicode
				# Render the screen
				self.screen.fill((0, 0, 0))
				self.screen.blit(background,(0,0))
				self.screen.blit(text1,text1_rect)
				pygame.draw.rect(self.screen, WHITE, input_rect, 2)
				input_text = font1.render(number, True, WHITE)
				self.screen.blit(input_text, (input_rect.x + 5, input_rect.y + 5))
				pygame.display.flip()
						
			while skin_sel:
				keys = pygame.key.get_pressed()
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					elif not confirm:
						image = pygame.image.load(f'./graphics/skin/{skin_index}/down_idle/down_0.png')
						self.screen.blit(background,(0,0))
						self.screen.blit(image,(WIDTH//2+200,HEIGHT//2-30))
						
					
						current_time = pygame.time.get_ticks()
						if not can_switch_skin:
							if current_time - skin_time >= skin_cooldown:
								can_switch_skin = True
						if keys[pygame.K_RIGHT] and can_switch_skin:
							can_switch_skin = False
							skin_time = pygame.time.get_ticks()
							if skin_index < 7 :
								skin_index += 1
							else:
								skin_index = 1 
						if keys[pygame.K_SPACE]:
							confirm = True
							run = True
							skin_sel= False
							self.level.player_data[0][1]= skin_index
				# Render the screen
				self.screen.blit(text3,text1_rect)
				self.screen.blit(text4,(WIDTH//2-200,HEIGHT//7*6))
				pygame.draw.rect(self.screen,(255,255,255),(WIDTH//2+190,HEIGHT//2-40,84,84),3)
				pygame.display.update()			
				
			# image loading
			resume_img  = pygame.image.load('./graphics/resume.png').convert_alpha()
			quit_img	= pygame.image.load('./graphics/quit.png').convert_alpha()
			audio_img   = pygame.image.load('./graphics/audio.png').convert_alpha()
			audio_gray  = pygame.image.load('./graphics/audio_gray.png').convert_alpha()
			
			resume_img   = pygame.transform.scale(resume_img,(400,125))
			quit_img     = pygame.transform.scale(quit_img,(400,125))
			audio_img    = pygame.transform.scale(audio_img,(400,125))
			audio_gray   = pygame.transform.scale(audio_gray,(400,125))
			#create button instances
			resume_button  = button.Button(WIDTH//2, HEIGHT//7*3, resume_img, 1)
			quit_button	= button.Button(WIDTH//2, HEIGHT//7*6, quit_img, 1)
			audio_normal   = button.Button(WIDTH//2, HEIGHT//7*4.5, audio_img, 1)
			audio_gray	 = button.Button(WIDTH//2, HEIGHT//7*4.5, audio_gray, 1)
			
			# audio control
			self.is_mute = False
			
			# sound 
			main_sound = pygame.mixer.Sound('./audio/main.ogg')
			main_sound.set_volume(0.5)
			main_sound.play(loops = -1)
			image = pygame.image.load('./graphics/GG.png')
			image = pygame.transform.scale(image,(800,800))	
				
			while run:
				while self.is_dead:
					
					self.screen.fill((255, 255, 255))
					self.screen.blit(image,(240,0))
					pygame.display.flip()
					
					if not self.is_mute:
						main_sound.stop()
					pygame.time.delay(3000)
					
					self.is_dead = False
					lobby =True 
					run = False
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
						self.screen.blit(menu,(WIDTH//2-175,70))
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
							self.save_game_data(number)
							if not self.is_mute:
								main_sound.stop()
				if not self.is_time_stopped:
					self.level.run()
				self.death_check()
				pygame.display.update()
				self.clock.tick(FPS)
				
if __name__ == '__main__':
	game = Game()
	game.run()
