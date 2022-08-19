import pygame

PIXELS=30
HOZ=int(720/30)
VET=int(870/30)

class Background:
	"""A class to represent the game background"""
	def __init__(self, sm_game):
		self.screen=sm_game.screen

	def draw(self, surface):
		"""draw the background on the screen"""
		surface.fill( (156, 210, 44) )
		counter = 0
		for row in range(VET):
			for col in range(HOZ):
				if counter % 2 == 0:
					pygame.draw.rect( surface, (147, 235, 57), (col * PIXELS, row * PIXELS, PIXELS, PIXELS) )
				if col != HOZ- 1:
					counter += 1
