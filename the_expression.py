import pygame
import numpy as np
import argparse

from Game_Data.UI import *

def setup():
    pygame.init()
    screen = pygame.display.set_mode()

    clock = pygame.time.Clock()
    
    return screen, clock

def draw(background, screen, clock, FPS):
    screen.fill((210,210,210))
    background.draw()
    
    menu.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()
    return 0


if __name__ == "__main__":
    
    exit = False
    FPS = 60

    screen, clock = setup()
    clock.tick(FPS)
    text = Text_Object(x = int(screen.get_rect()[2]/2.15), y = (screen.get_rect()[3] * 3)//4, size = 56, text = "Play", font = 'freesansbold.ttf')
    background = Animated_Background(screen = screen)
    menu = Main_Menu(screen)

    while (not(exit)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit = True
        draw(background, screen, clock, FPS)

    pygame.quit()
    quit
