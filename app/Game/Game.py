import pygame
from pygame.locals import *
from app.Screen.Screen import Screen

class Game:

    def __init__(self, screen_mounted: Screen, screen_surface) -> None:
        self.screen = screen_mounted
        self.screen_surface = screen_surface
        pass


    def run(self) -> None:
        pygame.init()

        sun_image = pygame.image.load('imgs/sun.png')
        bg_img = pygame.image.load('imgs/sky.png')

        run = True 
        while run:

            self.screen_surface.blit(bg_img, (0, 0))
            self.screen_surface.blit(sun_image, (100, 100))

            self.screen.draw_grid(200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()