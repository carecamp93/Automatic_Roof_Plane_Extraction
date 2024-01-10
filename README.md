# **Automatic Building Roof Plane Extraction in Urban Environments for 3D Modelling Using Remote Sensing data**

 This repository contains all the  scripts used in the development of the paper: "Automatic Building Roofs Planes Extraction in Urban Environments for 3D Modelling using Remote Sensing Data" (Remote Sensing MDPI, 2024), and the MSc. thesis: [AUTOMATIC BUILDING ROOF PLANE STRUCTURE EXTRACTION FROM REMOTE SENSING DATA FOR LOD2 3D CITY MODELLING](http://essay.utwente.nl/96138/) (ITC-UT, 2023).

Please use the following bib entry to cite the paper if you are using resources from this repo.

```
@article{Campoverde2024AutomaticRoofExtraction,
     title={Automatic Building Roofs Planes extraction in urban environ-ments for 3D modelling using Remote Sensing data},
     author={CCampoverde, Koeva, Persello, Maslov, Jiao, Petrova Antonova},
     booktitle={MDPI Remote Sensing},
     year={2024}
} 
```

If you wish to delve deeper into the details, you can consult the master's thesis, which delved extensively into this research. Please use the following bib entry to cite the MSc. thesis
```
@mastersthesis{campoverde2023automatic,
     title={Automatic building roof plane structure extraction from remote sensing data for lod2 3D city modelling},
     author={Campoverde, Carlos},
     year={2023},
     school={University of Twente}
} 
```



The presented work were developed on the top of the work developed by Chen, 2022 on the paper: HEAT: Holistic Edge Attention Transformer for Structured Reconstruction.

```
@inproceedings{chen2022heat,
     title={HEAT: Holistic Edge Attention Transformer for Structured Reconstruction},
     author={Chen, Jiacheng and Qian, Yiming and Furukawa, Yasutaka},
     booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
     year={2022}
} 
```
## **Introduction**

This paper presents a framework for Building inner roof planes reconstruction in aerial images and the application of the obtained outputs on LOD2 3D modelling.

Two different stages are presented:

1) Stage 1. Roof plane delineation/extraction
2) Stage 2. 3D Modelling

![INTRO1](./5.-PLOTS/Intro.svg)

As shown by the above figure, the overall framework consistes on two stages. Please refer to the paper or the Msc. Thesis for more details.

This repo provides the scripts, data, pre-trained checkpoints of HEAT on our study areas, and the 3D modelling metadata for de developed LOD2 3D model.

---
## **Study areas**

We have evaluated our framework in three different study areas: Stadsveld – 't Zwering, Enschede, Oude Mark, Enschede, both areas located in The Netherlands, and the neighborhood of Lozenets, Sofia, in Bulgaria. 

- The study area of Stadsveld – 't Zwering, located in the southern urban area of En-schede, The Netherlands, covers an area of around 153 hectares. The dataset contains 1972, 123, and 370 building samples for training validation and testing, respectively.

![AREA](./5.-PLOTS/studyarea1.jpg)

- The study area of Oude Markt, located in the central urban area of Enschede, The Netherlands, covers an area of around 6 hectares. The dataset contains 119 building samples for testing the whole workflow. 

![AREA2](./5.-PLOTS/studyarea2.jpg)

- The study area of Lozenets, located in the urban area of Sofia, Bulgaria, covers an area of around 812 hectares. The dataset contains 1440, 90, and 270 building samples for training, validation, and testing, respectively.

![AREA2](./5.-PLOTS/studyarea3.jpg)

Three study areas were defined with three main stages for its use have been defined, as shown belove.

![SPLIT](./5.-PLOTS/DatasetSplit.jpg)

---
## **Data**
Please download the data for the two stages from the links below. 

1) Stage 1. Roof plane delineation/extraction
Extract the data into the 1.- DATA PREPARATION/1.-INPUT

Data: https://drive.google.com/drive/folders/12AmomRCLc28QwAtFo-9YXQpJq4Q_FTAk?usp=drive_link


2) Stage 2. 3D Modelling

Data: https://drive.google.com/drive/folders/1C0qwlgx6gXsfIcFQd_x9gPT2yih6e-jf?usp=sharing

## **Checkpoints**
Please download the checkpoints for the different trained models from the link bellow
Extract the checpoints into the 2.- TRAINING-TESTING/checkpoints


Checkpoints: https://drive.google.com/drive/folders/1DMv5N5BE8Zcp8gLNU24Ylr9jZSnLxp9V?usp=sharing





#### Each script has its own purpose and requirements and should be run in this sequence of steps to reproduce the results in the MSc thesis:

## **Environment**

#### This repo was developed and tested with Jupiter Notebook using Python3.8
