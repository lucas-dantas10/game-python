import pygame
from pygame.locals import *
from app.Screen.Screen import Screen
from app.Game.Game import Game

def main():    
    game = Game()
    game.run()

if __name__ == '__main__':
    main()