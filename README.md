# The Expression - CMPT 419 Project
An Emotional Game for Social Expression Learning

![Demo](Demo.png)

## Requirements
- A webcam

## Dependencies
all the requirement dependencies are in requirements.txt

## Structure
the-expression.py is a driver to run the game
Model/model.ipynb is the testing and experimential with the proposed models, only the VGG16-VA was integrated to the main game
Dataset folder contains all the code to process the dataset, from restructuring original AFEW-VA dataset to extracted facial expressions and packing them into a single h5 file <br>

The processed dataset can be found [here](https://tinyurl.com/AFEW-VA-processed) <br>
the link included 
- a trained model using VGG16 transfer learning structure "trained_VGG16-VA.h5"
- an image dataset packed into h5 "facial_data.h5" (the README.md in the dataset folder has a guide to unpack this file)
- the true labels from AFEW-VA "label_data.csv"

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
