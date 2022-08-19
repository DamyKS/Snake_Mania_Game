import sys
import pygame
from time import sleep

from snake import Snake
from food import Food
from body import Body
from sm_settings import Settings
from sm_controls import Buttons
from sm_background import Background

class SnakeMania:
	"""A class to manage the snake game"""
	def __init__(self):
		"""Initialize the game and create game resources"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Snake Mania")
		
		
		self.background=Background(self)
		self.bodies=[  ]
		self.buttons=Buttons(self)
		self.snake=Snake(self)
		self.food=Food(self)
		
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			
			self.check_snake_food_collide()	
			self.move_body()
			self.check_snake_died()
			self.snake.update()
					
			self._update_screen()
			#to slow down the game 
			pygame.time.delay(120)
	
	def _check_events(self):
		"""A method to check for touchscreen events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
					
			elif event.type==pygame.MOUSEBUTTONDOWN:
				if self.buttons.right_rect.collidepoint(event.pos) and not self.snake.moving_left:
					self.snake.moving_right=True
					self.snake.moving_left=False
					self.snake.moving_up=False
					self.snake.moving_down=False
				elif self.buttons.left_rect.collidepoint(event.pos) and not self.snake.moving_right:
					self.snake.moving_left=True
					self.snake.moving_right=False
					self.snake.moving_up=False
					self.snake.moving_down=False
				elif self.buttons.up_rect.collidepoint(event.pos) and not self.snake.moving_down:
					self.snake.moving_up=True
					self.snake.moving_right=False
					self.snake.moving_left=False
					self.snake.moving_down=False
				elif self.buttons.down_rect.collidepoint(event.pos) and not self.snake.moving_up:
					self.snake.moving_down=True
					self.snake.moving_right=False
					self.snake.moving_left=False
					self.snake.moving_up=False	
										
	def check_snake_food_collide(self):
		"""check if the snake has eaten the food"""
		if self.food.dist_food_snake():
			self.food.update_food_pos()
			self.add_body()
	
	def draw_body(self):
		"""to draw al the available bodies"""
		if len(self.bodies) > 0:
			for body in self.bodies:
				body.draw()
	
	def add_body(self):
		"""to add a new body after the food's beem eater"""
		new_body = Body(self,self.snake.x, self.snake.y)
		self.bodies.append(new_body)
	
	def move_body(self):
		"""A method to move the snake bodies"""
		if len(self.bodies) > 0:
			#loop from end to start
			for i in range(len(self.bodies)-1,-1,-1):
				if i==0:
					#set the body pos to that of the snake
					self.bodies[i].body.x=self.snake.x
					self.bodies[i].body.y=self.snake.y			
				else:
					#set the body pos to that of the body in front of it
					self.bodies[i].body.x=self.bodies[i-1].body.x
					self.bodies[i].body.y=self.bodies[i-1].body.y
							
					
	def check_snake_died(self):
		"""check if the sbake has died and restart the game"""
		
		if self.snake.snake_hit_wall() or self.snake_hit_body():
			#delete all bodoes and reposition the snake and food
			while len(self.bodies)>0:
				self.bodies.pop()
			
			sleep(2)
			self.food.update_food_pos()
			self.snake.repos_snake()
	
	def snake_hit_body(self):
		"""to check if the snake head jas hit any of the bodies"""
		
		for i in range(1, len(self.bodies)):
			if self.bodies[i].dist_snake_body(self.snake.x, self.snake.y, self.bodies[i].body.x, self.bodies[i].body.y):
				return True
		
	def _update_screen(self):
		"""update images on the screen and flip to new screen"""
		self.background.draw(self.screen)
		self.buttons.display_buttons()
		
		self.draw_body()
		self.snake.display_snake()
		self.food.display_food()
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	sm=SnakeMania()
	sm.run_game()			
			