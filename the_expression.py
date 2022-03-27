from tkinter import Menu
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
    
    menu.update()
    menu.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()
    return 0


if __name__ == "__main__":
    
    exit = False
    FPS = 60

    screen, clock = setup()
    clock.tick(FPS)
    background = Animated_Background(screen = screen)
    menu = Main_Menu(screen)
    while (not(exit)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONUP and menu.buttons[1].state == 1):
                exit = True
            if (event.type == pygame.MOUSEBUTTONUP and menu.buttons[0].state == 1):
                menu = Game_Scene(screen)
        draw(background, screen, clock, FPS)

    pygame.quit()
    quit
