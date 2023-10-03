import pygame
from pygame.locals import *
from app.Screen.Screen import Screen
from app.Game.Game import Game

def main():

    screen_mounted = Screen(screen_width=1000 ,screen_height=600)
    screen = screen_mounted.set_mode()
    
    game = Game(screen_mounted, screen)
    game.run()

if __name__ == '__main__':
    main()