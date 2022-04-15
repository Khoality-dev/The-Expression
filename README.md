# The Expression - CMPT 419 Project
An Emotional Game for Social Expression Learning

![Demo](Demo.png)

## Requirements
- A webcam

## Dependencies
All the requirement dependencies are listed in requirements.txt

## Structure
Repository structure
- the-expression.py is a driver to run the game. <br>
- Model/model.ipynb is a notebook to test and do experimential with the proposed models, only the VGG16-VA was integrated to the main game. <br>
- Dataset folder contains all the code to process the AFEW-VA dataset, from restructuring original AFEW-VA dataset to extracted facial expressions and packing them into a single h5 file. <br>
- Game_Data/target_samples is the folder for customized target images, the images have to be processed using Dataset/game_target_generator.py before put in to this folder. (refering to Dataset/README.md for more details) <br>

The processed AFEW-VA dataset can be found [here](https://tinyurl.com/AFEW-VA-processed), the link included: <br>
- A trained model of VGG16 transfer learning structure "trained_VGG16-VA.h5"
- An image dataset packed into h5 "facial_data.h5" (the README.md in the dataset folder has more details to unpack this file)
- The true labels from AFEW-VA "label_data.csv"

## How to Use
- Setup a virtual environment
```bash
python -m venv [enviroment name]
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- To play
```bash
python the-expression.py
```

## Supported OS
Python version 3.7.8 on

- Windows 10 <br>
- Linux <br>
- MAC OS (Not tested) <br>
