import pygame
from pygame.locals import *
from pygame.surface import Surface

class Screen():

    def __init__(self) -> None:
        # SETUP
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Platformer')
        pass
    
    def draw_grid(self, tile_size) -> None:
        color_white = (255, 255, 255)
        for line in range(0, 20):
            pygame.draw.line(self.screen_surface, color_white, (0, line * tile_size), (self.screen_width, line * tile_size))
            pygame.draw.line(self.screen_surface, color_white, (line * tile_size, 0), (line * tile_size, self.screen_height))
    
    def get_surface(self):
        return pygame.display.get_surface()