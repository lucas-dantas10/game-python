from app.Game.Game import Game
import sys, os
from pytmx.util_pygame import load_pygame
import pygame
from settings.settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups) -> None:
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_rect(topleft = pos)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('./imgs/player.png')  # Load the player image
        self.rect = self.image.get_rect()
        self.speed = 5  # Set the initial speed (adjust as needed)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    tmx_data = load_pygame('./imgs/map.tmx')
    screen_group = pygame.sprite.Group()

    # Cicle through all layers
    mapa_largura = tmx_data.width * tmx_data.tilewidth
    mapa_altura = tmx_data.height * tmx_data.tileheight
    tela_largura, tela_altura = screen.get_size()

    posicao_inicial_x = (mapa_largura - tela_largura) // 2
    posicao_inicial_y = (mapa_altura - tela_altura) // 2


    for layer in tmx_data.visible_layers:
        if hasattr(layer, 'data'):
            for x, y, surface in layer.tiles():
                pos = (x * 32 - posicao_inicial_x, y * 32 - posicao_inicial_y)
                Tile(pos=pos, surf=surface, groups=[screen_group])


    
    player = Player(10, 10)  # Set initial position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0)
        if keys[pygame.K_UP]:
            player.move(0, -1)
        if keys[pygame.K_DOWN]:
            player.move(0, 1)
                
        screen_group.draw(screen)
        screen_group.update()
        player.draw(screen)

        pygame.display.flip()



    # game = Game()
    # game.run()

if __name__ == '__main__':
    main()