import argparse
import os
from alive_progress import alive_bar
import h5py

from utils.imglib import load_image, load_images

def packer(args):
    data_dir = args.src
    target_h5 = args.dst
    img_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg')]
    h5_file = h5py.File(target_h5, "w")
    print("Packing up dataset...")
    with alive_bar(len(img_files)) as bar:
        for file_name in img_files:
            img = load_image(os.path.join(data_dir, file_name), grey_scale = False)
            h5_file.create_dataset(file_name, data = img)
            bar()
    print("Done!")
    h5_file.close()
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', dest = 'src', default = "facial_data")
    parser.add_argument('-dst', dest = 'dst', default = "facial_data.h5")
    args = parser.parse_args()
    packer(args)