import pygame
import numpy as np
import argparse

from Game_Data.UI import Bubble_Object

def setup():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800,600), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    
    return screen, clock

def draw(screen, clock, FPS, bubble_list):

    clock.tick(FPS)
    screen.blit(background, (0,0))
    
    for bubble_idx in range(len(bubble_list)):
        if bubble_list[bubble_idx].on_screen == False:
            bubble_list[bubble_idx] = Bubble_Object(x = np.random.randint(0,800), y = np.random.randint(600,1200), r = np.random.randint(5,20), color=(10,240,240))
        bubble_list[bubble_idx].update()
        bubble_list[bubble_idx].draw(screen = screen)
    pygame.display.update()
    return 0


if __name__ == "__main__":
    
    exit = False
    FPS = 60

    screen, clock = setup()
    clock.tick(FPS)

    background = pygame.image.load('Game_Data/background/blue.png')
    bubble_list = []
    for i in range(50):
        bubble = Bubble_Object(x = np.random.randint(0,800), y = np.random.randint(0,620), r = np.random.randint(5,20), color=(10,240,240))
        bubble_list.append(bubble)

    while (not(exit)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit = True
        draw(screen, clock, FPS, bubble_list)

    pygame.quit()
    quit
