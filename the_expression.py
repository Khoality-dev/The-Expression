import pygame
import pygame.camera
import numpy as np
import argparse

from Game_Data.UI import *

def setup():
    pygame.init()
    pygame.camera.init()
    screen = pygame.display.set_mode()
    print(pygame.camera.list_cameras())
    cam_device = pygame.camera.list_cameras()[0]
    camera = pygame.camera.Camera(cam_device)
    print(camera.get_size())
    camera.start()
    clock = pygame.time.Clock()
    
    return screen, camera, clock

def draw(background, screen, clock, FPS):
    background.draw()
    
    menu.update()
    menu.draw(screen)

    screen.blit(pygame.transform.flip(camera.get_image(), flip_x= True, flip_y= False), (0,0))
    clock.tick(FPS)
    pygame.display.update()
    return 0


if __name__ == "__main__":
    screen, camera, clock = setup()

    exit = False
    FPS = 60

    
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
