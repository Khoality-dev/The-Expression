import os

from alive_progress import alive_bar
import cv2
from utils.imglib import load_image
import argparse

def extractor(args):

    if not(os.path.isfile(args.detector_model)):
        print("ERROR: Detector model does not exist!")
        return 1

    #Init Haar cascades
    detector = cv2.CascadeClassifier(args.detector_model)
    data_dir = args.src
    target_dir = args.dst
    os.makedirs(target_dir, exist_ok=True)
    target_H = args.height
    target_W = args.width

    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg')]
    print("Extracting faces from images...")
    with alive_bar(len(img_files)) as bar:
        for img_name in img_files:
            if not(os.path.isfile(os.path.join(target_dir, os.path.splitext(img_name)[0] + "_0.png"))): #Extract only image that has not been extracted
                img = load_image(os.path.join(data_dir, img_name), grey_scale = False)

                faces = detector.detectMultiScale(img)  #Detect face in image
                face_idx = 0
                for face in faces:
                    (x, y, w, h) = face
                    crop_img = img[y:y+h, x:x+w]
                    crop_img = cv2.resize(crop_img, (target_H,target_W))    #Resize image into target size
                    face_filename = os.path.join(target_dir, os.path.splitext(img_name)[0] + "_" + str(face_idx) + ".png") 
                    cv2.imwrite(face_filename, crop_img) #save image to target_dir
                    face_idx += 1
            bar()
    print("Done!")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', dest = 'src', default = "src_data")
    parser.add_argument('-H', dest = 'height', default = 256)
    parser.add_argument('-W', dest = 'width', default = 256)
    parser.add_argument('-dst', dest = 'dst', default = "facial_data")
    parser.add_argument('-dmodel', dest = 'detector_model', default = "utils/haarcascade_frontalface_alt2.xml")
    args = parser.parse_args()
    extractor(args)

    