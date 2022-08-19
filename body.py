import pygame
from random import randint
import math

class Body:
	"""A class to represent a single snake body"""
	def __init__(self, sm_game,posx,posy):
		"""initialoze the body and set it's syarting pos"""
		super().__init__()
		
		self.screen=sm_game.screen
		self.snake=sm_game.snake
		
		self.body= pygame.Rect((0, 0), (30, 30))
		self.body.x=posx
		self.body.y=posy
		
	def dist_snake_body(self, x_2,y_2, x_1,y_1):
		
		distance= math.sqrt(math.pow( (x_2 - x_1),2)+ math.pow( (y_2 - y_1),2))
		if distance<30:
			return True	
		
	def draw(self):
		"""draw the body to the screen"""
		self.screen.fill((0,0,230), self.body)
					