from app.Game.Game import Game
import sys, os
from pytmx.util_pygame import load_pygame
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups) -> None:
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('imgs/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

def main():    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    tmx_data = load_pygame('./imgs/map.tmx')
    sprite_group = pygame.sprite.Group()

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
                Tile(pos=pos, surf=surface, groups=sprite_group)

    player = Player(pos=(10, 10), groups=sprite_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        keys = pygame.key.get_pressed()
        player.direction = pygame.math.Vector2(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

        player.rect.move_ip(player.direction * 5) 
        
        screen.fill('black')
        sprite_group.draw(screen)
        sprite_group.update()
        pygame.display.update()



    # game = Game()
    # game.run()

if __name__ == '__main__':
    main()