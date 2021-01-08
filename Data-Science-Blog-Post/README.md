# Singapore apartment resale prices analysis
## Project motivation
A large dataset containing informaton resale prices of apartments in Singapore was analyzed following Cross-Industry Standard Process of Data Mining (CRISP-DM) methodology.
The purpose of this analysis is to provide answers to the following business questions:

* Which is the district of Singapore with the highest average apartment resale price per square meter?
* Apart from the district, which other features significantly affect the resale price?
* Which is a reasonable resale price for an apartment in Singapore with specific characteristics?

## Attached files
This repository contains the following files:
* A copy of the original dataset, named [SG_prices.csv](SG_prices.csv). 
* A [Jupyter Notebook](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Data-Science-Blog-Post/Singapore%20apartment%20resale%20prices%20analysis.ipynb), which contains the Python code that was used for this project. The code makes use of the following Python libraries: 
  * pandas
  * numpy
  * matplotlib
  * seaborn
  * scipy
  * sklearn
  
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
For more information about the limitations at translating and detecting languages of a given text using the feature langdetect please refer to this [.txt document] ().



## Conclusions
Findings and conclusions from this analysis are presented in this [Medium post](https://luis-conti-gz.medium.com/singapore-apartment-resale-prices-analysis-1105770b3015). 
Summarizing:
* Singapore Central Area has the highest apartment resale prices per square meter.
* Several features affect the price of the apartment: size, location, floor level, apartment type, apartment model and, to a lesser extent, lease commence date.
* The multiple lineal model built in Python showed a very good performance and robustness at estimating the resale price of an apartment in Singapore given some characteristics.

## Licensing, Authors, Acknowledgements
* The origina dataset was downloaded from the [Singaporean Government website](https://data.gov.sg/dataset/resale-flat-prices?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
