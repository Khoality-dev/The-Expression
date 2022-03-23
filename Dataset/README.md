# Data Preprocessing
This module is to format the structure of AFEW-VA dataset and extract faces from frames.

## How to use
- To clean the structure, the module will move all images data from sub folders of "AFEW-VA" to one single folder and join all the arousal-valence data to a single label_data.csv
```bash
python ./AFEW-VA_formatter.py
```
- To extract facial images from AFEW-VA images above
```bash
python ./AFEW-VA_extractor.py -src [path of source] -dst [path of destination] -H [target height] -W [target width] -dmodel [path of facial detection model]
```
- To extract facial images from customized dataset
```bash
python ./extractor.py -src [path of source] -dst [path of destination] -H [target height] -W [target width] -dmodel [path of facial detection model]
```
- To pack facial images into single h5 file
```bash
python ./packer.py -src [path of source] -dst [path of destination]
```
## Citing
* J. Kossaifi, G. Tzimiropoulos, S. Todorovic and M. Pantic. AFEW-VA for valence and arousal estimation In-The-Wild. Image and Vision Computing, 2016 (submitted).
*  Abhinav Dhall, Roland Goecke, Simon Lucey, and Tom Gedeon. Static Facial Expressions in Tough Conditions: Data, Evaluation Protocol And Benchmark, First IEEE International Workshop on Benchmarking Facial Image Analysis Technologies BeFIT, IEEE International Conference on Computer Vision ICCV2011, Barcelona, Spain, 6-13 November 2011


