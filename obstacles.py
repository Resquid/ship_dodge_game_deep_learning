import pygame
from pygame.sprite import Sprite
import random
class Obstacle(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super(Obstacle,self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(100,100,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = random.randint(0,1200)
		self.rect.bottom = 0
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	def update(self):
		self.y += self.speed_factor
		self.rect.y = self.y
	
	def draw_obstacle(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
