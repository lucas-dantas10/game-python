import pygame
from pygame.locals import *
from app.Screen.Screen import Screen
from settings.settings import *

class World(Screen):

    def __init__(self) -> None:
        self.tile_list = []
        self.tile_size = TILE_SIZE

        world_data = WORLD_MAP

        dirt_img = pygame.image.load('imgs/dirt.png')
        grass_img = pygame.image.load('imgs/grass.png')
        
        row_count = 0
        for row in world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        screen = super().get_surface()
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])