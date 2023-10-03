import pygame
from pygame.locals import *
from pygame.surface import Surface

class Screen():

    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Platformer')
        pass

    def set_mode(self) -> Surface:
        return self.screen_surface
    
    def draw_grid(self, tile_size) -> None:
        color_white = (255, 255, 255)
        for line in range(0, 20):
            pygame.draw.line(self.screen_surface, color_white, (0, line * tile_size), (self.screen_width, line * tile_size))
            pygame.draw.line(self.screen_surface, color_white, (line * tile_size, 0), (line * tile_size, self.screen_height))
    
    def get_surface(self):
        return pygame.display.get_surface()