# Disaster Response Pipeline
## Project motivation
The purpose of this project is to build a model for an API that classifies disaster messages. Those messages can be, for example, tweets sent during a natural disaster such as earthquakes or hurricanes. A machine learning pipeline will categorize these messages so that they can be sent to the appropriate disaster relief agency.


## Attached files
This repository contains the following files:
* Two datasets, in .csv format, provided by [Figure Eight (now Appen)](https://appen.com/figure-eight-is-now-appen/):
  * [disaster_messages.csv](disaster_messages.csv): contains original messages sent during disasters. 
  * [disaster_categories.csv](disaster_categories.csv): contains a classification of the beforehand mentioned messages.
  
* Two scripts, that are run in a terminal:
  * [process_data.py](XXX): Reads the datasets, merges them, cleans the data and stores the resulting dataframe in a SQLite database.
  * [train_classifier.py](XXX): Makes use of the SQLite database created by process_data.py to create and tune a machine learning pipeline model. Additionally, this script evaluates the model and stored it as a pickle file.  
  
* Two Jupyter Notebooks that were used as a support at creating process_data.py and train_classifier.py scripts:
  * [ETL Pipeline Preparation.ipynb](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/ETL%20Pipeline%20Preparation.ipynb): Used as support for the development of process_data.py.
  * [ML Pipeline Preparation.ipynb](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/ML%20Pipeline%20Preparation.ipynb): Used as support for the development of train_classifier.py.

## Conclusions
Findings and conclusions from this analysis are presented in this [Medium post](https://luis-conti-gz.medium.com/singapore-apartment-resale-prices-analysis-1105770b3015). 
Summarizing:
* Singapore Central Area has the highest apartment resale prices per square meter.
* Several features affect the price of the apartment: size, location, floor level, apartment type, apartment model and, to a lesser extent, lease commence date.
* The multiple lineal model built in Python showed a very good performance and robustness at estimating the resale price of an apartment in Singapore given some characteristics.

## Licensing, Authors, Acknowledgements
* Original datasets are provided by [Figure Eight (now Appen)](https://appen.com/figure-eight-is-now-appen/) to [Udacity](https://www.udacity.com).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.

