# What does it contain?
This repository contains the final project for the course
"Introduction to Python for Data Analysis and Automation in Biology”.

## Description
### Background
For my PhD reserach, I working with deep learning method for pathology detection in capsule endoscopy using bounding boxes annotations.
One of the open source dataset I am using is Kvasir Capsule (https://osf.io/dv2ag/). Kvasir Capsule is a large capsule endoscopy dataset collected from examinations at Hospitals in Norway. Kvasir-Capsule consists of 117 videos which can be used to extract a total of 4,741,504 image frames. They have labelled and medically verified 47,238 frames with a bounding box around detected anomalies from 14 different classes of findings..
For my work I consider images from the eight most representative pathology classes amounting to a total of 3,365 images with their ground truth annotations.
We convert the dataset annoations into a coco JSON file which we use for the analysis in this code.

### Structure of the coco JSON file
The coco JSON file containing the dataset annotations has a structure as follows ( This is just an example of an image annotation):

![image](https://github.com/user-attachments/assets/299e9f4f-35c0-42a0-baa0-1a58fabc4e3d)


### Objective
The objective of this code is to provide a rapid analysis of the dataset and help have an overview of its contents.
This code can be used to get an overview of the content of any dataset which coco annotation JSON file is provide.
We mainly analyse the coco JSON file containing the annotations for the 8 pathological classes we considered, and provide the following:
1) The total Number of image
2) The annotations per category (class)
3) The histogram of number of annotations per pathology
4) The list of images having a given pathology

### Requirement
Install few libraries for python such as:
- install matplotlib
- install numpy
  
### Run the code
```shell script
           python jsonfile.py
    ```


