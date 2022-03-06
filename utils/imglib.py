from keras.preprocessing import image
import os
import numpy as np
import h5py
import cv2

def h5_load_image(h5, key):
    return h5['key'].value

def h5_load_images(h5, keys):
    img_list = []
    for key in keys:
        img_list.append(h5[key].value)
    return img_list

def load_image(data_dir, W, H):
    img_load = cv2.imread(data_dir)

    return img_load

def load_images(data_dir, W, H):
    img_list = []
    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    for f in img_files:
        img_load = cv2.imread(os.path.join(data_dir,f))
        img_list.append(img_load)
    return img_list

def load_sampling(data_dir,name_files, W, H):
    img_list = []
    img_files = name_files
    for f in img_files:
        img_load = cv2.imread(os.path.join(data_dir,f))
        img_list.append(img_load)
    return img_list