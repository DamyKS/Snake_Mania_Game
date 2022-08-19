import pygame
from random import randrange

class Snake:
	def __init__(self, sm_game):
		"""A class to manage the snake"""
		super().__init__()
		self.settings = sm_game.settings
		self.screen=sm_game.screen
		self.screen_rect=sm_game.screen.get_rect()
		self.snake= pygame.Rect((0, 0), (30, 30))
		self.snake.x=120
		self.snake.y= 390
		
		self.x=self.snake.x
		self.y=self.snake.y
		
		self.moving_right=True
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		
	def update(self):
		"""to update the position of the snake"""
		if self.moving_right==True:
			self.x +=self.settings.snake_speed
		if self.moving_left==True:
			self.x-=self.settings.snake_speed
		if self.moving_up==True:
			self.y -=self.settings.snake_speed
		if self.moving_down==True:
			self.y +=self.settings.snake_speed
			
		self.snake.x = self.x
		self.snake.y= self.y
	
	def snake_hit_wall(self):
		"""to check if the snake has hit the wall"""
		if self.snake.x<0 or self.snake.x>690 or self.snake.y<0 or self.snake.y>840:
			return True
		
	def repos_snake(self):
		"""Reposition the snake to it's starting point"""
		
		self.x=120
		self.y=390
		
		self.moving_right=True
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False

	def display_snake(self):
		"""To dtaw the snake on the screen"""
		self.screen.fill((0,0,0), self.snake)
		