import pygame
import pygame.camera
import numpy as np
import argparse
import os

from Game_Data.UI import *
from Model.models import AV_Estimator, Face_Detector, Facial_Landmark_Detector

def camera_setup():
    pygame.camera.init()
    list_pycam = pygame.camera.list_cameras()

    if (len(list_pycam) == 0):
        print("ERROR: No camera detected!")
        return False

    os.system('cls||clear')
    print("List camera available:")
    for camera_idx in range(len(list_pycam)):
        print(camera_idx,". ",list_pycam[camera_idx], sep = '')

    while (True):
        pycamera = input("Enter camera number: ")
        if int(pycamera) >= len(list_pycam) or int(pycamera) < 0:
            print("ERROR: Camera is not available!")
        else:
            break
    pycamera = pygame.camera.Camera(list_pycam[int(pycamera)])
    pycamera.start()
    
    camera = Camera(pycamera, flip_x = False, flip_y = False, rotating_state = 0)
    return camera

def setup():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode()
    
    
    clock = pygame.time.Clock()
    
    return screen, clock


camera = camera_setup()
screen, clock = setup()
background = Animated_Background(screen = screen)
menu = Main_Menu(screen)


#FLD = Facial_Landmark_Detector()

#AV = AV_Estimator()
#AV.load_weights("Model/trained_model.h5")


def update():
    menu.update()

def draw():
    background.draw(screen)
    
    menu.draw(screen)
    
    pygame.display.update()
    return 0


if __name__ == "__main__":

    exit = False
    FPS = 60

    
    current_menu = 0
    while (not(exit)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if (current_menu == 0):
                if (event.type == pygame.MOUSEBUTTONUP and menu.buttons[0].on_hover()):
                    current_menu = 1
                    menu = Play_Menu(camera, screen)
                elif (event.type == pygame.MOUSEBUTTONUP and menu.buttons[1].on_hover()):
                    current_menu = 2
                    menu = Camera_Menu(camera, screen)
                elif (event.type == pygame.MOUSEBUTTONUP and menu.buttons[2].on_hover()):
                    exit = True
            elif (current_menu == 2):
                if (event.type == pygame.MOUSEBUTTONUP and menu.buttons[0].on_hover()):
                    camera.rotate()
                elif (event.type == pygame.MOUSEBUTTONUP and menu.buttons[1].on_hover()):
                    camera.flip_on_x()
                elif (event.type == pygame.MOUSEBUTTONUP and menu.buttons[2].on_hover()):
                    camera.flip_on_y()
                elif (event.type == pygame.MOUSEBUTTONUP and menu.buttons[3].on_hover()):
                    current_menu = 0
                    menu = Main_Menu(screen)
        
        update()
        draw()
        clock.tick(FPS)

    pygame.quit()
    quit
