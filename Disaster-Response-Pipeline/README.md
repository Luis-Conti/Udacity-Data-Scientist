# Disaster Response Pipeline
## Project motivation
The purpose of this project is to build a model for an API that classifies disaster messages. These messages can be, for example, news published in an online newspaper or tweets sent during a natural disaster such as earthquakes or hurricanes. A machine learning pipeline will categorize these messages so that they can be sent to the appropriate disaster relief agency.

## Attached files
This repository contains the following files:
* Two datasets, in .csv format, provided by [Figure Eight (now Appen)](https://appen.com/figure-eight-is-now-appen/):
  * [disaster_messages.csv](disaster_messages.csv): contains original messages sent during disasters. 
  * [disaster_categories.csv](disaster_categories.csv): contains a classification of the beforehand mentioned messages.
  
* Three scripts, that are run in a terminal:
  * [process_data.py](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/process_data.py): Reads the datasets, merges them and cleans the data  by means of an ETL Pipeline, and stores the resulting dataframe in a SQLite database.
  * [train_classifier.py](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/train_classifier.py): Makes use of the SQLite database created by process_data.py to create and tune a Machine Learning Pipeline model. Additionally, this script evaluates the model and stored it as a pickle file.  
  * [run.py](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/run.py): Launches the API web that makes use of the machine learning model created in the previous step.
  
* Two Jupyter Notebooks that were used as a support at creating process_data.py and train_classifier.py scripts:
  * [ETL Pipeline Preparation.ipynb](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/ETL%20Pipeline%20Preparation.ipynb): Used as support for the development of process_data.py.
  * [ML Pipeline Preparation.ipynb](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/ML%20Pipeline%20Preparation.ipynb): Used as support for the development of train_classifier.py. In this Notebook, a grid search was performed with multiple combinations of up to 4 parameters in order to optimize the accuracy of the resulting pipeline. In order to save time when creating the Machine Model in the terminal, pipeline in train_classifier.py is already defined with these optimal parameters.
  
## Instructions to run the web app
1. Go to the project's root directory. There:
 * Run the ETL pipeline (process_data.py). This will clear the input datasets, merge them and store the resulting dataset in a database. In order to have the correct inputs, run the following piece of code: `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
 * Run the ML pipeline (train_classifier.py). This will create a model that will allow us classify disaster response messages. The model will be saved in a .pkl file. In order to have the correct inputs, run the following piece of code: `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
2. Go to the web app directory. There:
 * Install the langdetect package by executing the following command line: `! pip install langdetect`
 * Run the web app by executing the following command line: `python run.py`
 * Go to http://0.0.0.0:3001/ (alternatively, if you have problems, try with http://localhost:3001 in a browser). You will be redirected to the web app.
3. In the web app, enter a disaster response message (in English language) and press "Classify message". The message will be classified in different categories depending on its content.

## Web app overview
You will be able to insert your message (in English language) in the search bar shown in the following picture:

![alt text](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/Screenshots/Web%20App%20search%20bar.PNG)

Once the text is entered, and after clicking "Classify Message", a list of all categories will appear. Those categories related to the entered text will be highlighted in green, as shown in the picture below:

![alt text](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/Screenshots/Web%20App%20pic%201.PNG)

Besides the message classification feature, the web app offers interesting statistics about the dataset that was used to train the model:
1. The percentage of messages corresponding to each genre (direct, news and social):
![alt text](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/Screenshots/Web%20App%20pic%202.png)


2. A bar chat showing the number of messages sent by category:
![alt text](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/Screenshots/Web%20App%20pic%203.PNG)

3. A bar chat showing, for the most common languages of the original messages, the number of messages for each genre:
![alt text](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Disaster-Response-Pipeline/Screenshots/Web%20App%20pic%204.png)


## Language detection limitation and alternatives

The identification of the language of the different texts contained in the column "original" of the [disaster_messages.csv](disaster_messages.csv) dataset has been performed by means of the langdetect Python functionality.
Unfortunately, the accuracy of langdetect at detecting is not very good for languages that are not among the most common in the world (English, Chinese, Spanish, etc.). As as 
consequence, languages such as Haitian Creole is not properly identified. Actually, it is not even among the languages included in langdetect. See [langdetect documentation](https://pypi.org/project/langdetect/). It is important to point out that the results shown in the bar plots do not represent the actual languages included in the dataset, due to these langdetect limitations.

There are a lot of alternatives. For example, using [googletrans](https://pypi.org/project/googletrans/). This Python library makes use of Google Translate API. It was confirmed that languages are properly detected (even less common languages like Haitian Creole). However, this function has a limitation in term of the number of request that are possible. When googletrans was implemented in this project in order to translate all the rows of the "original" column of the database that are not empty (over 10000), the following error was obtained: 'Translator' object has no attribute 'raise_Exception'. For a lower number of texts to be translated (or whose language is desired to be detected), googletrans is a good option.

In order to have access to a higher number of translate/language detection requests, a suscription to [Google cloud services](https://cloud.google.com/translate/docs/reference/libraries/v3/python) would be the best option. As this is not a free service, and as translationa and language detection are not the main topics of this project, the use of Google Cloud Services for language detection will not be made.



## Licensing, Authors, Acknowledgements
* Original datasets are provided by [Figure Eight (now Appen)](https://appen.com/figure-eight-is-now-appen/) to [Udacity](https://www.udacity.com).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.

