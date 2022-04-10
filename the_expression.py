import pygame
import pygame.camera
import numpy as np
import argparse
import os

from Game_Data.UI import *
from Model.models import AV_Estimator, Face_Detector

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
    
    return pycamera

def setup():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode()
    pygame.mixer.init()
    
    clock = pygame.time.Clock()
    
    return screen, clock

AV = AV_Estimator(path = "Model/best_model.h5")
FD = Face_Detector()

pycamera = camera_setup()
screen, clock = setup()
camera = Camera(screen, pycamera, flip_x = False, flip_y = False, rotating_state = 0)
background = Animated_Background(screen = screen)
menu = Main_Menu(screen)
click_sound = pygame.mixer.Sound("Game_Data/sound/mixkit-game-click-1114.wav")
bgms = ["Game_Data/sound/bensound-acousticbreeze.mp3", "Game_Data/sound/bensound-jazzyfrenchy.mp3"]
pygame.mixer.music.load(bgms[0])
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()


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
            if (event.type == pygame.MOUSEBUTTONUP):
                flag = 0
                if (current_menu == 0):
                    if (menu.buttons[0].on_hover()):
                        current_menu = 1
                        menu = Play_Menu(AV, FD, camera, screen)
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load(bgms[1])
                        pygame.mixer.music.play()
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        flag = 1

                    elif (menu.buttons[1].on_hover()):
                        current_menu = 2
                        menu = Camera_Menu(camera, screen, FD)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        flag = 1

                    elif (menu.buttons[2].on_hover()):
                        exit = True
                        flag = 1

                elif (current_menu == 1):
                    if (menu.round.isEnd()):
                        if (menu.buttons[0].on_hover()):
                            menu = Play_Menu(AV, FD, camera, screen)
                            pygame.mixer.music.unload()
                            pygame.mixer.music.load(bgms[1])
                            pygame.mixer.music.play()
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            flag = 1
                        elif (menu.buttons[1].on_hover()):
                            current_menu = 0
                            menu = Main_Menu(screen)
                            pygame.mixer.music.unload()
                            pygame.mixer.music.load(bgms[0])
                            pygame.mixer.music.play()
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            flag = 1 
                elif (current_menu == 2):
                        if (menu.buttons[0].on_hover()):
                            camera.rotate()
                            flag = 1
                        elif (menu.buttons[1].on_hover()):
                            camera.flip_on_x()
                            flag = 1
                        elif (menu.buttons[2].on_hover()):
                            camera.flip_on_y()
                            flag = 1
                        elif (menu.buttons[3].on_hover()):
                            current_menu = 0
                            menu = Main_Menu(screen)
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            flag = 1

                if (flag == 1):
                    click_sound.play()
        
        update()
        draw()
        clock.tick(FPS)

    pygame.quit()
    quit
