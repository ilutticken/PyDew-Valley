import pygame
from settings import *
import sys

class MainMenu:
	def __init__(self, start_game):
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font('font/LycheeSoda.ttf', 50)
		self.start_game = start_game
		self.options = ["Start Game", "Options", "Quit"]
		self.selected_index = 0

	def display(self):
		self.display_surface.fill('black')
		for index, option in enumerate(self.options):
			color = 'White' if index == self.selected_index else 'Gray'
			text_surf = self.font.render(option, True, color)
			text_rect = text_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + index * 60))
			self.display_surface.blit(text_surf, text_rect)

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.selected_index = (self.selected_index - 1) % len(self.options)
		elif keys[pygame.K_DOWN]:
			self.selected_index = (self.selected_index + 1) % len(self.options)
		elif keys[pygame.K_RETURN]:
			if self.selected_index == 0:
				self.start_game()
			elif self.selected_index == 2:
				pygame.quit()
				sys.exit()

	def update(self):
		self.input()
		self.display()
