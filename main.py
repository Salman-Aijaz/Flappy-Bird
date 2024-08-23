import sys
import pygame
from pygame.locals import *
from constants import *
from game_functions import *

if __name__ == "__main__":
    pygame.init()
    framepersecond_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')

    load_game_images()  

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or enter to start the game")

    while True:
        horizontal = int(window_width / 5)
        vertical = int((window_height - game_images['flappybird'].get_height()) / 2)
        print("flappy bird heihgt",game_images["flappybird"].get_height())
        ground = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'], (horizontal, vertical))
                    window.blit(game_images['sea_level'], (ground, elevation))
                    pygame.display.update()
                    framepersecond_clock.tick(framepersecond)
