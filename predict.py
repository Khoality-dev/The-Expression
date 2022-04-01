import argparse
import numpy as np
import cv2
import os
import random
import dlib
import pandas as pd
import tensorflow as tf

def get_random_target_image():

    path = "Dataset/game_data"

    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    return random_filename

def get_landmarks(face):

    landmarks_detection = dlib.shape_predictor('Dataset/utils/shape_predictor_68_face_landmarks.dat')

    landmarks = landmarks_detection(face, dlib.rectangle(0,0,63,63))
    list_landmarks = []
    for i in range(0, 68):
        list_landmarks.append(landmarks.part(i).x)
        list_landmarks.append(landmarks.part(i).y)
  
    return list_landmarks

def load_images_from_folder(folder):

    face_detection = cv2.CascadeClassifier('Dataset/utils/haarcascade_frontalface_alt2.xml')

    images = []
    landmarks = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            detected_faces = face_detection.detectMultiscale(gray_image)

            if(len(detected_faces) > 1): continue

            (x,y,w,h) = detected_faces[0]
            
            cropped_image = gray_image[y:y+h,x:x+w]
            cropped_image = cv2.resize(np.array(cropped_image), (64,64))

            landmarks.append(get_landmarks(cropped_image))
            images.append(gray_image)
    return np.array(images), np.array(landmarks)

def decide_winner(target,predictions_0,predictions_1):

    best_0 = 0
    best_1 = 0
    winner = -1

    for i in range(len(predictions_0)):
        dist_0 = np.linalg.norm(target - predictions_0[i])
        if(best_0 > dist_0): best_0 = dist_0

        dist_1 = np.linalg.norm(target - predictions_1[i])
        if(best_1 > dist_1): best_1 = dist_1

    if(best_0 > best_1): winner = 0
    elif(best_0 < best_1): winner = 1
    else: winner = 2

    return winner, best_0, best_1

def predict(args):

    model = tf.keras.models.load_model(args.m)
    images_0, landmarks_0 = load_images_from_folder(args.d1)
    images_1, landmarks_1 = load_images_from_folder(args.d2)
    df = pd.read_csv('../Dataset/src_data/label_data.csv')
    df = df.loc[df['file_name'] == args.t]
    target = df[['arousal', 'valence']].values

    predictions_0 = model.predict([images_0, landmarks_0])
    predictions_1 = model.predict([images_1, landmarks_1])

    return decide_winner(target=target,predictions_0=predictions_0,predictions_1=predictions_1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest = 'model_path', default = "/models")
    parser.add_argument('-d0', dest = 'data_path_0', default = "/dataset")
    parser.add_argument('-d1', dest = 'data_path_1', default = "/dataset")
    parser.add_argument('-t', dest = 'target_path', default = "Dataset/game_data")
    args = parser.parse_args()
    predict(args)
