from json.tool import main
import cv2
import tensorflow as tf
import pandas as pd
import numpy as np
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
        self.detector = dlib.shape_predictor('Dataset/utils/shape_predictor_68_face_landmarks.dat')

    def predict(self, input_img):
        facical_landmarks = self.detector(input_img, dlib.rectangle(0,0,len(input_img[0]), len(input_img[0])))
        list_landmarks = []
        for i in range(0, 68):
            list_landmarks.append(facical_landmarks.part(i).x)
            list_landmarks.append(facical_landmarks.part(i).y)
        return list_landmarks

class AV_Estimator():
    def __init__(self,path):
        self.model = tf.keras.models.load_model(path)

    def predict(self, x, y):
        return self.model.predict([np.resize(x,(1,64,64)), np.resize(y,(1,136))])

class New_Game():
    def __init__(self, img_name):

        df = pd.read_csv('../Dataset/src_data/label_data.csv')
        df = df.loc[df['file_name'] == img_name]
        self.target = df[['arousal', 'valence']].values

        self.face_detector = Face_Detector()
        self.shape_predictor = Facial_Landmark_Detector()
        self.estimator = AV_Estimator()
        self.best_0 = 0
        self.best_1 = 0

    def get_current_best(self):
        return self.best_0, self.best_1

    def estimate(self,img_0,img_1):
        cropped_img_0 = self.face_detector.predict_crop(img_0)
        cropped_img_1 = self.face_detector.predict_crop(img_1)

        if(cropped_img_0 != None and cropped_img_1 != None):
            facical_landmarks_0 = self.shape_predictor.predict(cropped_img_0)
            facical_landmarks_1 = self.shape_predictor.predict(cropped_img_1)
            if(len(facical_landmarks_0) != 0 and len(facical_landmarks_1) != 0):
                pred_0 = self.estimator.predict([cropped_img_0, facical_landmarks_0])
                pred_1 = self.estimator.predict([cropped_img_1, facical_landmarks_1])

                dist_0 = np.linalg.norm(self.target - pred_0)
                dist_1 = np.linalg.norm(self.target - pred_1)

                if(dist_0 < self.best_0): self.best_0 = dist_0
                if(dist_1 < self.best_1): self.best_1 = dist_1

                return pred_0, pred_1

        return None

    def winner(self):
        if(self.best_0 > self.best_1): return 0
        elif(self.best_1 > self.best_0): return 1
        else: return -1

if __name__ == "__main__":
    av = AV_Estimator('../models/best_model.h5')
    print(av.model.summary())