import os
import cv2
import numpy as np
import pygame
from Model.models import *
from Dataset.utils.imglib import load_image

def load_and_get_random_img(data_dir = "Game_Data/target_samples"):
    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg')]

    return cv2.cvtColor(load_image(os.path.join(data_dir,np.random.choice(img_files))), cv2.COLOR_BGR2RGB)

def get_score(player_AV, target_AV):
    return np.linalg.norm(player_AV - target_AV)

class Match():
    def __init__(self, camera, FDetector, AVEstimator, length_in_milisec):
        self.state = 0
        self.start_time = 0
        self.camera = camera
        self.AVEstimator = AVEstimator
        self.FDetector = FDetector
        self.length = length_in_milisec
        self.current_time = pygame.time.get_ticks()
        self.player_1_best_face = []
        self.player_2_best_face = []
        self.player_1_best_score = 10
        self.player_2_best_score = 10
        self.player_1_score = 10
        self.player_2_score = 10

        self.isFace_p1 = False
        self.isFace_p2 = False

        #self.bgm_victory = pygame.mixer.Sound("Game_Data/sound/fiftysounds-sfx-victory5.mp3")

        self.target = np.array(load_and_get_random_img())
        target_face = self.FDetector.predict_crop(self.target)
        #target_landmarks = self.FLDetector.predict(target_face)
        self.target_AV = self.AVEstimator.predict(target_face)*10
        return
    
    def start(self):
        self.state = 1
        self.start_time = pygame.time.get_ticks()
        return

    def isEnd(self):
        return (self.state==2)

    def get_countdown(self):
        return max(self.length - (self.current_time - self.start_time), 0)
  

    def update(self):
        if (self.state == 1):
            if (self.get_countdown() <= 0):
                self.state = 2
                #pygame.mixer.music.unload()
                #self.bgm_victory.play()

            if not(self.isEnd()):
                self.current_time = pygame.time.get_ticks()

                cam1, cam2 = self.camera.get_output_transform()

                img_cam1 = cv2.rotate(pygame.surfarray.array3d(cam1), cv2.ROTATE_90_CLOCKWISE)
                self.isFace_p1 = False
                img_cam1 = self.FDetector.predict_crop(np.array(img_cam1))
                self.player_1_score = 10
                if (len(img_cam1) != 0):
                    self.isFace_p1 = True
                    #landmarks_cam1 = self.FLDetector.predict(img_cam1)
                    cam1_AV = self.AVEstimator.predict(img_cam1)*10
                    self.player_1_score = get_score(cam1_AV, self.target_AV)
                    if (self.player_1_best_score > self.player_1_score):
                        self.player_1_best_score = self.player_1_score
                        self.player_1_best_face = cam1
                else:
                    self.isFace_p1 = False

                img_cam2 = cv2.rotate(pygame.surfarray.array3d(cam2), cv2.ROTATE_90_CLOCKWISE)
                img_cam2 = self.FDetector.predict_crop(np.array(img_cam2))
                self.player_2_score = 10
                if (len(img_cam2) != 0):
                    self.isFace_p2 = True
                    #landmarks_cam2 = self.FLDetector.predict(img_cam2)
                    cam2_AV = self.AVEstimator.predict(img_cam2)*10
                    self.player_2_score = get_score(cam2_AV, self.target_AV)
                    if (self.player_2_best_score > self.player_2_score):
                        self.player_2_best_score = self.player_2_score
                        self.player_2_best_face = cam2
                else:
                    self.isFace_p2 = False
                
        return