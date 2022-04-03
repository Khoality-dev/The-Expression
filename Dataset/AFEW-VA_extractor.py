import os

from alive_progress import alive_bar
import cv2
from utils.imglib import load_image
import argparse
import pandas as pd

def landmark_inbox(x, y, w, h, landmarks):
    cnt = 0
    for landmark_idx in range(68):
        if (x <= landmarks[2*landmark_idx] and landmarks[2*landmark_idx] <= x+w):
            if (y <= landmarks[2*landmark_idx+1] and landmarks[2*landmark_idx+1] <= y+h):
                cnt+=1
    return cnt

def extractor(args):

    if not(os.path.isfile(args.detector_model)):
        print("ERROR: Detector model does not exist!")
        return 1

    detector = cv2.CascadeClassifier(args.detector_model)

    data_dir = args.src
    target_dir = args.dst

    os.makedirs(target_dir, exist_ok=True)

    target_H = args.height
    target_W = args.width

    landmarks = pd.read_csv(os.path.join(args.src,"label_data.csv"))

    file_names = landmarks.iloc[:,int(landmarks.columns.get_loc('file_name'))].to_numpy()
    landmarks = landmarks.iloc[:,int(landmarks.columns.get_loc('landmark_x_0')):int(landmarks.columns.get_loc('landmark_y_67')+1)].to_numpy()

    print("Extracting faces from images")

    idx = 0
    with alive_bar(len(file_names)) as bar:
        for label_idx in range(len(file_names)):
            img_name = file_names[label_idx]
            if not(os.path.isfile(os.path.join(target_dir, os.path.splitext(img_name)[0] + ".png"))):
                if (os.path.isfile(os.path.join(data_dir,img_name))):
                    img = load_image(os.path.join(data_dir, img_name), grey_scale = True)
                    faces = detector.detectMultiScale(img)
                    best_n_landmarks = 0
                    (best_x, best_y, best_w, best_h) = (-1,-1,-1,-1)
                    for face in faces:
                        (x, y, w, h) = face
                        n_landmark_points = landmark_inbox(x,y,w,h, landmarks[idx])
                        if (best_n_landmarks < n_landmark_points):
                            best_n_landmarks = n_landmark_points
                            (best_x, best_y, best_w, best_h) = (x, y, w, h)
                    if ((best_x, best_y, best_w, best_h) != (-1,-1,-1,-1)):
                        crop_img = img[best_y:best_y+best_h, best_x:best_x+best_w]
                        crop_img = cv2.resize(crop_img, (target_H,target_W))
                        face_filename = os.path.join(target_dir, os.path.splitext(img_name)[0] + ".png")
                        cv2.imwrite(face_filename, crop_img)
            idx += 1
            bar()
    print("Done!")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', dest = 'src', default = "src_data")
    parser.add_argument('-H', dest = 'height', default = 64)
    parser.add_argument('-W', dest = 'width', default = 64)
    parser.add_argument('-dst', dest = 'dst', default = "facial_data")
    parser.add_argument('-dmodel', dest = 'detector_model', default = "utils/haarcascade_frontalface_alt2.xml")
    args = parser.parse_args()
    extractor(args)

    