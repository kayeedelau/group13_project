import pygame
from pygame import font

# game setup
WIDTH = 1280
HEIGHT = 800
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player':-26,
	'ob':-40,
	'01':-10,
	'02':-10,
	'invisible':0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './graphics/font/joystix.ttf'
UI_FONT_SIZE = 20


# genarl colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'
BLACK = (0,0,0)
WHITE = (255,255,255)
color1 = (0,100,100)
color2 = (100,150,0)

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons 
weapon_data = {
	'sword'  :{'cooldown':100, 'damage':15,'graphic':'./graphics/weapon/sword/full.png'},
	'lance'  :{'cooldown':400, 'damage':30,'graphic':'./graphics/weapon/lance/full.png'},
	'axe'	:{'cooldown':300, 'damage':20,'graphic':'./graphics/weapon/axe/full.png'},
	'rapier' :{'cooldown': 50, 'damage':8 ,'graphic':'./graphics/weapon/rapier/full.png'},
	'sai'	:{'cooldown': 80, 'damage':10,'graphic':'./graphics/weapon/sai/full.png'}}
	
#magic
magic_data ={
 'flame' : {'strength':5,'cost': 20, 'graphic':'./graphics/flame/fire.png'},
 'heal' :  {'strength':20,'cost': 10, 'graphic':'./graphics/heal/heal.png'},
 'teleport': {'strength':0,'cost':30,'graphic':'./graphics/teleport.png'}}
 
#enemy
monster_data = {
	'squid' :{'health':100, 'exp':100, 'damage':20,'attack_type':'slash','attack_sound':'./audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':80,'notice_radius':360},
	'raccoon' :{'health':300, 'exp':250, 'damage':40,'attack_type':'claw','attack_sound':'./audio/attack/claw.wav','speed':2,'resistance':3,'attack_radius':120,'notice_radius':400},
	'spirit' :{'health':100, 'exp':110, 'damage':8,'attack_type':'thunder','attack_sound':'./audio/attack/fireball.wav','speed':4,'resistance':3,'attack_radius':60,'notice_radius':350},
	'bamboo' :{'health':70, 'exp':120, 'damage':6,'attack_type':'leaf_attack','attack_sound':'./audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':50,'notice_radius':300}}
