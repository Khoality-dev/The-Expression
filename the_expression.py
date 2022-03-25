import pygame
import numpy as np
import argparse

from Game_Data.UI import *

def setup():
    pygame.init()
    screen = pygame.display.set_mode()

    clock = pygame.time.Clock()
    
    return screen, clock

def draw(background, logo, screen, clock, FPS):
    screen.fill((210,210,210))
    background.draw()
    screen.blit(logo, (int(screen.get_rect()[2]/3.5),0))
    
    text.update()
    text.draw(screen)
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
    logo = pygame.image.load("Game_Data/image/The Expression-logos_transparent.png")
    logo = pygame.transform.scale(logo, (800,800))

    while (not(exit)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit = True
        draw(background, logo, screen, clock, FPS)

    pygame.quit()
    quit
