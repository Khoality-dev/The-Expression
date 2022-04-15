# Data Preprocessing
This module is to format the structure of AFEW-VA dataset and extract faces from frames.

## How to use

### Only use for AFEW-VA dataset
- To clean the structure, the module will move all images data from sub folders of "AFEW-VA" to one single folder and join all the arousal-valence data to a single label_data.csv
```bash
python ./AFEW-VA_formatter.py
```
For example: putting all the scene folders into a subfolder named "AFEW-VA", running above command will create a new folder named "src_data" and move all the images into that folder.

- To extract facial images from AFEW-VA images above
```bash
python ./AFEW-VA_extractor.py -src [path of source] -dst [path of destination] -H [target height] -W [target width]
```
For example: python ./AFEW-VA_extractor.py -src src_data -dst facial_data -H 64 -W 64. <br>

### Other type of dataset
- To extract facial images from customized dataset
```bash
python ./extractor.py -src [path of source] -dst [path of destination] -H [target height] -W [target width]
```
For example: python ./extractor.py -src src_data -dst facial_data -H 64 -W 64. <br>

- To pack facial images into single h5 file
```bash
python ./packer.py -src [path of source] -dst [path of destination]
```
For example: python ./packer.py -src facial_data -dst facial_data.h5 <br>

- To unpack facial images from h5 file
```bash
python ./unpacker.py -src [path of h5 file] -dst [path of destination]
```
For example: python ./unpacker.py -src facial_data.h5 -dst facial_data <br>

- To create customized target image
```bash
python ./game_target_generator.py -src [path of source] -dst [path of destination]
```
For example: python ./game_target_generator.py -src src_data -dst game_data <br>
After processing the customized target image, you may want to copy all the image to ../Game_Data/target_samples <br>

## Citing
* J. Kossaifi, G. Tzimiropoulos, S. Todorovic and M. Pantic. AFEW-VA for valence and arousal estimation In-The-Wild. Image and Vision Computing, 2016 (submitted).
*  Abhinav Dhall, Roland Goecke, Simon Lucey, and Tom Gedeon. Static Facial Expressions in Tough Conditions: Data, Evaluation Protocol And Benchmark, First IEEE International Workshop on Benchmarking Facial Image Analysis Technologies BeFIT, IEEE International Conference on Computer Vision ICCV2011, Barcelona, Spain, 6-13 November 2011


