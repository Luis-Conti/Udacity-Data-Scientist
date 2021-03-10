# Turbofan Health Monitoring and Predictive Maintenance
## Project motivation
The aim of this portfolio is to develop and discuss methodologies and algorithms to monitor the health status and carry out predictive maintenance on commercial aircraft engines based only on the information gathered by the sensors installed throughout the engine. For such purpose, a large amount of data from a turbofan model, with different flight and degradation conditions on different components of the engine, have been analyzed. If the model is accurate enough and, it is possible to build mathematical models that could allow airline operators to identify and isolate degradation in the engines of their fleets by analyzing in-service data. By doing this, it is possible to avoid unnecessary stops for MRO (Maintenance, repair and overhaul), prevent higher fuel consumption due to degradation of some components or even major incidents.

Two different approach will be discussed and compared:

* Polynomial regression, degree 2 and 3
* Neural networks

Data from the model have been obtained from the [NASA website](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/).

## Attached files
This repository contains the following files:
* A copy of the original dataset, named [SG_prices.csv](SG_prices.csv). 
* A [Jupyter Notebook](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Data-Science-Blog-Post/Singapore%20apartment%20resale%20prices%20analysis.ipynb), which contains the Python code that was used for this project.

  
## Installation
For the correct deployment of the different scripts, Python 3.x (ideally Python 3.6) shall be installed. Following libraries are also necesarry:
  * pandas
  * numpy
  * matplotlib
  * sqlite3
  * sklearn
  * SQLalchemy
  * json
  * flask
  * sys 
  * pickle
  * langdetect  
  
## Translate & Language detection limitations
For more information about the limitations at translating and detecting languages of a given text using the feature langdetect please refer to this [txt document] ().



## Conclusions
Findings and conclusions from this analysis are presented in this [Medium post](https://luis-conti-gz.medium.com/singapore-apartment-resale-prices-analysis-1105770b3015). 
Summarizing:
* Singapore Central Area has the highest apartment resale prices per square meter.
* Several features affect the price of the apartment: size, location, floor level, apartment type, apartment model and, to a lesser extent, lease commence date.
* The multiple lineal model built in Python showed a very good performance and robustness at estimating the resale price of an apartment in Singapore given some characteristics.

## Licensing, Authors, Acknowledgements
* The origina dataset was downloaded from the [Singaporean Government website](https://data.gov.sg/dataset/resale-flat-prices?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
