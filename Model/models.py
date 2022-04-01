import cv2
import tensorflow as tf
from keras.layers import Conv2D, BatchNormalization, AvgPool2D, Dropout, Dense, Flatten, Concatenate
from keras.models import Sequential
from keras.optimizers import Adam
import dlib

class Face_Detector():
    def __init__(self):
        self.detector = cv2.CascadeClassifier("Dataset/utils/haarcascade_frontalface_alt2.xml")
        self.target_W, self.target_H = 64,64

    def predict(self, input_img):
        faces = self.detector.detectMultiScale(input_img)
        if (len(faces)>0):
            (x, y, w, h) = faces[0]
            return x, y, w, h
        return None

    def predict_crop(self, input_img):
        faces = self.detector.detectMultiScale(input_img)
        if (len(faces)>0):
            (x, y, w, h) = faces[0]
            crop_img = input_img[y:y+h, x:x+w]
            crop_img = cv2.resize(crop_img, (self.target_W, self.target_H))
            return crop_img
        return None

class Facial_Landmark_Detector():
    def __init__(self):
        self.detector = dlib.shape_predictor('../Dataset/utils/shape_predictor_68_face_landmarks.dat')

    def predict(self, input_img):
        facical_landmarks = self.detector(input_img, dlib.rectangle(0,0,len(input_img), len(input_img[0])))
        return facical_landmarks

class AV_Estimator():
    def __init__(self):
        self.input_shape = (64,64)
        self.output_shape = (2,)

        model = Sequential()

        model.add(Conv2D(16, kernel_size=(3,3), activation='relu', padding='same'))
        model.add(BatchNormalization())
        model.add(Conv2D(16, kernel_size=(3,3), activation='relu', padding='same'))
        model.add(BatchNormalization())

        model.add(AvgPool2D(strides=(2,2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(32, kernel_size=(3,3), activation='relu', padding='same'))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=(3,3), activation='relu', padding='same'))
        model.add(BatchNormalization())

        model.add(AvgPool2D(strides=(2,2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.25))

        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.4))

        model.add(Dense(2, activation='linear'))

        self.model = model


    def load_weights(self, path):
        self.model.load_weights(path)

    def predict(self, x):
        return self.model.predict(x)

