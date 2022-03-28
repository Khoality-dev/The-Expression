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

def draw(background, camera, screen, clock, FPS):
    background.draw()
    
    menu.update()
    menu.draw(screen)
    (cam_width, cam_height) = camera.get_size()
    cam_image = pygame.transform.flip(camera.get_image(), flip_x = True, flip_y = False)
    first_cam = pygame.transform.chop(cam_image, (cam_width/2, 0, cam_width/2,0))
    second_cam = pygame.transform.chop(cam_image, (0, 0, cam_width/2,0))
    screen.blit(first_cam, (30,30))
    screen.blit(second_cam, (1000,30))
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
    current_menu = 0
    while (not(exit)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONUP and menu.buttons[1].state == 1):
                exit = True
            if (current_menu == 0):
                if (event.type == pygame.MOUSEBUTTONUP and menu.buttons[0].state == 1):
                    current_menu = 1
                    menu = Game_Scene(screen)
        draw(background, camera, screen, clock, FPS)

    pygame.quit()
    quit
