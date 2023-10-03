import pygame
from pygame.locals import *
from app.Screen.Screen import Screen
from app.World.World import World

class Game:

    def __init__(self, screen_mounted: Screen, screen_surface) -> None:
        # VARIABLES OF AMBIENT
        self.screen = screen_mounted
        self.screen_surface = screen_surface
        self.tile_size = 50
        pass


    def run(self) -> None:
        pygame.init()

        world = World(self.tile_size)

        run = True 
        while run:

            self.add_main_images()

            world.draw()

            self.screen.draw_grid(self.tile_size)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()

    def add_main_images(self):
        sun_image = pygame.image.load('imgs/sun.png')
        bg_img = pygame.image.load('imgs/sky.png')

        self.screen_surface.blit(bg_img, (0, 0))
        self.screen_surface.blit(sun_image, (100, 100))