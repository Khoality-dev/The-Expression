import os

from alive_progress import alive_bar
import cv2
from utils.imglib import load_image
import argparse

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
    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg')]
    print("Extracting faces from images")
    with alive_bar(len(img_files)) as bar:
        for img_name in img_files:
            img = load_image(os.path.join(data_dir, img_name), W = target_W, H = target_H, grey_scale = False)
            faces = detector.detectMultiScale(img)
            if (len(faces)!=0):
                cv2.imwrite(os.path.join(target_dir, img_name), img)
            else:
                print("Unrecognized any face in", img_name)
            bar()
    print("Done!")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', dest = 'src', default = "src_data")
    parser.add_argument('-H', dest = 'height', default = 320)
    parser.add_argument('-W', dest = 'width', default = 480)
    parser.add_argument('-dst', dest = 'dst', default = "game_data")
    parser.add_argument('-dmodel', dest = 'detector_model', default = "utils/haarcascade_frontalface_alt2.xml")
    args = parser.parse_args()
    extractor(args)

    