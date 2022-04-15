#This module is to unpack the h5 file into image files
import argparse
import os

import cv2
import numpy as np
from alive_progress import alive_bar
import h5py

from utils.imglib import load_image, load_images

def unpacker(args):
    src_h5 = args.src
    target_dir = args.dst
    os.makedirs(target_dir, exist_ok = True)
    h5_file = h5py.File(src_h5, "r")
    print("Unpacking dataset...")
    with alive_bar(len(h5_file.keys())) as bar:
        for key in h5_file.keys():
            img = np.array(h5_file[key])
            cv2.imwrite(os.path.join(target_dir,str(key)), img)
            bar()
    print("Done!")
    h5_file.close()
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', dest = 'src', default = "facial_data.h5")
    parser.add_argument('-des', dest = 'dst', default = "facial_data")
    args = parser.parse_args()
    unpacker(args)