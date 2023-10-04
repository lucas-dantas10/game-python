import pygame
from pygame.locals import *
from app.Screen.Screen import Screen
from app.World.World import World
from settings.settings import *

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.running = True


    def run(self) -> None:

        while self.running:

            self.add_main_images()

            self.handle_draw()

            self.handle_events()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def add_main_images(self):
        sun_image = pygame.image.load('imgs/sun.png')
        bg_img = pygame.image.load('imgs/sky.png')

        self.screen.get_surface().blit(bg_img, (0, 0))
        self.screen.get_surface().blit(sun_image, (100, 100))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def handle_draw(self):
        world = World()
        world.draw()
        self.screen.draw_grid()