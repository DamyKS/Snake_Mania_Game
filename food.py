import pygame
from random import randrange
import math

class Food:
	"""A class to manage the snake food"""
	def __init__(self, sm_game):
		
		self.screen=sm_game.screen
		self.snake=sm_game.snake
		self.screen_rect=sm_game.screen.get_rect()
		self.food= pygame.Rect((0, 0), (30, 30))
		self.food.x= randrange(0,720,30)
		self.food.y= randrange(0,840,30)
	
	def update_food_pos(self):
		"""to generate a new position gor the snake"""
		self.food.x= randrange(0,720,30)
		self.food.y= randrange(0,840,30)
		
	def dist_food_snake(self):
		"""to change the food's ppsition after it's eaten"""
		distance= math.sqrt(math.pow( (self.snake.x - self.food.x),2)+ math.pow( (self.snake.y - self.food.y),2))
		if distance <30:
			return True	
		

	def display_food(self):
		"""draw the food on the scrren"""
		self.screen.fill((230,0,0), self.food)
	
	