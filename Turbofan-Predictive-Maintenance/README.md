# Turbofan Health Monitoring and Predictive Maintenance
## Project motivation
The aim of this portfolio is to develop and discuss methodologies and algorithms to monitor the health status and carry out predictive maintenance on commercial aircraft engines based only on the information gathered by the sensors installed throughout the engine. For such purpose, a large amount of data from a turbofan model, with different flight and degradation conditions on different components of the engine, have been analyzed. If the model is accurate enough and, it is possible to build mathematical models that could allow airline operators to identify and isolate degradation in the engines of their fleets by analyzing in-service data. By doing this, it is possible to avoid unnecessary stops for MRO (Maintenance, repair and overhaul), prevent higher fuel consumption due to degradation of some components or even major incidents.

Two different approach will be discussed and compared:

* Polynomial regression, degree 2 and 3
* Neural networks

Data from the model have been obtained from the [NASA website](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/).

## Attached files
This repository contains the following files:
* A [Jupyter Notebook](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Turbofan-Predictive-Maintenance/Turbofan%20health%20monitoring%20and%20predictive%20maintenance.ipynb), which contains the Python code that was used for this project.

  
## Installation
For the correct deployment of the different scripts, Python 3.x (ideally Python 3.6) shall be installed. Following libraries are also necesarry:
  * pandas
  * numpy
  * matplotlib
  * sklearn
  * seaborn
  * os
  * h5py
  * keras

## Instructions
1- Download the dataset to your working environment from this [link](https://mega.nz/folder/1F5zySrR#CIQGD4VjC2IY9ZRJF_c3pg)
2- Download the [Jupyter Notebook](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Turbofan-Predictive-Maintenance/Turbofan%20health%20monitoring%20and%20predictive%20maintenance.ipynb) to your working folder.
3- Execute all command lines of the Jupyter Notebook. It might take a couple of hours to execute all the code lines.


## Blog post
Project depelopment process and conclusions are available in this [Medium post](https://luis-conti-gz.medium.com/XXXX). 


## Licensing, Authors, Acknowledgements
* [Análisis de metodologías para la identificación de la degradación en turbinas de gas. Aplicación en el motor Rolls-Royce RB211](http://bibing.us.es/proyectos/abreproy/60315/fichero/Memoria_Proyecto.pdf). Conti González, Luis Manuel. Universidad de Sevilla. 2015.
* "Run_to_Failure_Simulation_Under_Real_Flight_Conditions_Dataset". Chao, Manuel A.; Kulkarni, Chetan; Goebel, Kai; Fink, Olga. 2020. 
* Datasets are available in the [Data repository of the NASA website](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
