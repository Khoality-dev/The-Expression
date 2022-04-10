import cv2
from cv2 import COLOR_BGR2GRAY
import tensorflow as tf
import pandas as pd
import numpy as np

from keras.applications.vgg16 import preprocess_input

target_W = 64
target_H = 64
target_landmarks = 136

class Face_Detector():
    def __init__(self):
        self.detector = cv2.CascadeClassifier("Dataset/utils/haarcascade_frontalface_alt2.xml")
        self.target_W, self.target_H = 64,64

    def predict(self, input_img):
        faces = self.detector.detectMultiScale(cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY))
        if (len(faces)>0):
            (x, y, w, h) = faces[0]
            return [x, y, w, h]
        return []

    def predict_crop(self, input_img):
        faces = self.detector.detectMultiScale(cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY))
        if (len(faces)>0):
            (x, y, w, h) = faces[0]
            crop_img = input_img[y:y+h, x:x+w]
            crop_img = cv2.resize(crop_img, (self.target_W, self.target_H))
            return crop_img
        return []

class AV_Estimator():
    def __init__(self,path):
        self.model = tf.keras.models.load_model(path)

    def predict(self, x):
        img = np.resize(x,(1,target_W,target_H,3))
        img = preprocess_input(img)
        return np.reshape(self.model.predict(img),(2,))
