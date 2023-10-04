import pygame
from pygame.locals import *
from settings.settings import *

class Screen():

    def __init__(self) -> None:
        self.screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('GAME')
    
    def draw_grid(self) -> None:
        color_white = (255, 255, 255)
        for line in range(0, 20):
            pygame.draw.line(self.screen_surface, color_white, (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
            pygame.draw.line(self.screen_surface, color_white, (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))
    
    def get_surface(self):
        return pygame.display.get_surface()