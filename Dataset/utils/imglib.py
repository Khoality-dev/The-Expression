import os
import h5py
import cv2
import numpy as np
from alive_progress import alive_bar

def h5_load_image(h5, key):
    return h5['key'].value

def h5_load_images(h5, keys):
    img_list = []
    for key in keys:
        img_list.append(h5[key].value)
    return img_list

def h5_load_image_all(h5_file_path):
    img_list = []
    h5_file = h5py.File(h5_file_path, "r")
    with alive_bar(len(h5_file.keys())) as bar:
        for key in h5_file.keys():
            img_list.append(np.array(h5_file[key]))
            bar()
    return img_list


def load_image(data_dir, W = None, H = None, grey_scale = False):
    flag = cv2.IMREAD_COLOR
    if (grey_scale):
        flag = cv2.IMREAD_GRAYSCALE

    img_load = cv2.imread(data_dir, flag)
    if (W != None and H!= None):
        img_load = cv2.resize(img_load, (W,H))

    return img_load

def load_images(data_dir, W = None, H = None, grey_scale = False):
    img_list = []
    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg')]
    flag = 1
    if (grey_scale):
        flag = 0
    for f in img_files:
        img_load = []
        img_load = cv2.imread(os.path.join(data_dir,f),flag)
        if (W != None and H!= None):
            img_load = cv2.resize(img_load, (W,H))
        img_list.append(img_load)
    return img_list

def load_sampling(data_dir,name_files, W = None, H = None, grey_scale = False):
    img_list = []
    img_files = name_files
    flag = 1
    if (grey_scale):
        flag = 0
    for f in img_files:
        img_load = cv2.imread(os.path.join(data_dir,f),flag)
        if (W != None and H!= None):
            img_load = cv2.resize(img_load, (W,H))
        img_list.append(img_load)
    return img_list

