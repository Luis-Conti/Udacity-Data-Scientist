
# Recommendation Engines IBM
## Project motivation
The aim of this project is to develop different recommendation engines to provide users different articles they may have interest in. A real case study has been developed, using data from [IBM Watson](https://dataplatform.cloud.ibm.com/home?context=wdp). Different solutions have been discussed:

* Rank-based recommendations
* Content-based recommendations
* Matrix factorization

## Attached files
This repository contains the following files:
* A [Jupyter Notebook](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Recommendation-Engines-IBM/Recommendations_with_IBM.ipynb), which contains the Python code that was used for this project.
* A [.html file](https://github.com/Luis-Conti/Udacity-Data-Scientist/blob/main/Recommendation-Engines-IBM/Recommendations_with_IBM.html), also containing the Python code that was used for this project.

  
## Installation
The following Python libraries were used for the development of this project:
  * pandas
  * numpy
  * matplotlib
 
 ## Analysis and development process
 The following steps were followed throughout the development of the project:
 ### I. Exploratory Data Analysis
 In order to have a better oveview of the data, an exploratory analysis of them is carried out.
 ### II. Rank-Based Recommendations
 A recommendation engine based entirely on the popularity of the articles available on the IBM platform is developed to provide users recommendation on new articles.
 ### III. User-User Based Collaborative Filtering
 In this section, two different versions of collaborative filtering recommendation engines are developed. They try to identify similar users among the datasets to recommend users new articles that they have not yet interacted with.
 ### IV. Content-based recommendation
 This section was not developed. This can be considered a future improvement of this set of recommendation engines. For this purpose, NLP (Natural Language Processing) algorithms can be very useful.
 ### V. Matrix Factorization.
 Matrix decomposition will be applied with the goal of building a model that predicts suitable recommendation to users, with different number of latent factors.
 
 ## Conclusions
Following conclusion can be drawn from the project:
* Rank-based recommendations work for all new users and users that have already interact with a huge number of articles. However, and as expected due to the nature of this kind of engines, recommendations are not personalized and may recommend articles users are not interested in, at all.
* User-user based collaborative filtering engines are able to identify users that are interested in similar topics, and therefore able to provide better recommendations. However, they are not able to provide any recommendation to user that have not interacted with any article yet. This is the so-called "cold start problem" and, for these new users, the unique option is a rank-based recommendation engine.
* Thanks to a matrix factorization method called SVD (Single Value Decomposition), it was possible to create a model to provide recommendations. Accuracy of the model is satisfactory, but the impact of the number of latent factors in the accuracy is almost negligable.

## Licensing, Authors, Acknowledgements
* The datasets that were used during this project correspond to real data that were kindly provided by [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio).
* The content of this post is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
