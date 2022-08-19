import pygame

class Buttons:
	"""A class of buttons to move the ship"""
	def __init__(self,sm_game):
		self.screen=sm_game.screen
		#lower  screen boundary
		self.boundary_rect=pygame.Rect((0, 0), (840, 5))
		self.boundary_rect.y=870
		
		#left button
		self.left_rect=pygame.Rect((0, 0), (90, 90))
		self.left_rect.center=(470, 1090)
		#right button
		self.right_rect=pygame.Rect((0, 0), (90, 90))
		self.right_rect.center=(600, 1090)
		#down button
		self.down_rect=pygame.Rect((0, 0), (90, 90))
		self.down_rect.center=(535, 1200)
		#up button
		self.up_rect=pygame.Rect((0, 0), (90, 90))
		self.up_rect.center=(535, 980)
		
		
		#button direction signs
		myfont = pygame.font.SysFont('Arial', 60)
		self.dir_sign_1= myfont.render("««", 1, (255, 255, 255))
		self.dir_sign_2= myfont.render("»»", 1, (255, 255, 255))
		
	def display_buttons(self):
		"""display  the buttons for all directioms"""
		#left & right 
		self.screen.fill((0, 0, 0), self.left_rect)
		self.screen.fill((0, 0, 0), self.right_rect)
		#down & up
		self.screen.fill((0, 0, 0), self.down_rect)
		self.screen.fill((0, 0, 0), self.up_rect)
		
		#boundary
		self.screen.fill((0, 0, 0), self.boundary_rect)
		
		#direction signs
		self.screen.blit(self.dir_sign_1 , (435, 1050))
		self.screen.blit(self.dir_sign_2 ,  (570,1050))
	
	