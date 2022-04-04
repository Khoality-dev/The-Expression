import time
import cv2
import numpy as np
import pygame.camera
import pygame
from sklearn.preprocessing import StandardScaler
from Dataset.utils.imglib import load_image

from Model.models import AV_Estimator, Face_Detector, Facial_Landmark_Detector

pygame.camera.init()
pycamera = pygame.camera.Camera(pygame.camera.list_cameras()[0])
pycamera.start()
time.sleep(1)

x = pygame.surfarray.array3d(pygame.transform.flip(pycamera.get_image(), flip_x= True, flip_y= False))
img_cam1 = cv2.rotate(cv2.cvtColor(x, cv2.COLOR_RGB2GRAY), cv2.ROTATE_90_CLOCKWISE)

AV = AV_Estimator("Model/best_model.h5")
FD = Face_Detector()
FLD = Facial_Landmark_Detector()

face_1 = FD.predict_crop(img_cam1)
landmarks = FLD.predict(face_1)
pred_1 = AV.predict(face_1/127.5 - 1,landmarks)
print("Player:", pred_1)

target_img = load_image("Game_Data/target_samples/unknown.png", grey_scale= True)
face = FD.predict_crop(target_img)
landmarks = FLD.predict(face)
pred_2 = AV.predict(face/127.5 - 1,landmarks)
print("Target:", pred_2)

print(np.linalg.norm(pred_1 - pred_2))

cv2.imshow("test",face)
cv2.waitKey(0)