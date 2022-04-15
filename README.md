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
Dataset folder contains all the code to process the dataset, from restructuring original AFEW-VA dataset to extracted facial expressions and packing them into a single facial_data.h5 <br>
The processed dataset can be found [here](tinyurl.com/AFEW-VA-processed)

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
