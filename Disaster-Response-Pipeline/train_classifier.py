import sys
import re
import numpy as np
import pandas as pd
import nltk
import pickle
import sqlite3
nltk.download(['punkt', 'wordnet'])
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
from sklearn.metrics import classification_report
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
#from sklearn.preprocessing import StandardScaler

def load_data(database_filepath):
    
    ''' Load a database and provides attribute variable, target variables and headers corresponding to target variables
    
    INPUT:
    database_filepath - path of the .db file (database) created and stored by the process_data.py script
   
    
    OUTPUT:
    X - dataframe corresponding to the attribute variable (1 column, that corresponds to the text contained in the disaster_message.csv file which is input of the process_data.py script)
    Y - dataframe corresponding to the target variables (36 columns, correspond to each value of the "categories" column contained in the categories_message.csv file which is input of the                     process_data.py script) 
    category_names - headers of the Y dataframe

    '''
    
    engine = create_engine('sqlite:///{}'.format(database_filepath))
   
    df = pd.read_sql_table('DisasterResponseTable', engine) 
    
    df = df.replace(to_replace='None', value=np.nan)
    
    df=df[df["message"]!='#NAME?']
    
    X = df["message"] 
    Y = df.loc[:,"related":"direct_report"]
    
    category_names = Y.columns
    
    return X, Y, category_names
        

def tokenize(text):
    
    ''' Tokenizes and normalizes the input text, removes stop words and symbols apart from letters and numbers
    
    INPUT:
    df- a text (string format)
      
    
    OUTPUT:
    clear tokens- a list of strings, obtained as a result of the following operations on the input text:
            - Everything but letters (uppercase und lowercase) and numbers will be removed
            - Text will be divided into separate elements, or "tokens"
            - Stop words corresponding to the English language will be removed
            - Tokens will be lemmatized, i.e. tokens will be converted into "root words",
                based on WordNetLemmatizer
            - Tokens will be lemmatized, i.e. tokens will be converted into "root words"
            - Tokens will be normalized
   
    '''
    
    # normalize text
    text = re.sub(r"[^a-zA-Z0-9]"," ",text)
    
    # tokenize text
    tokens = word_tokenize(text)
    
    # remove tokens corresponding to stop words
    tokens = [word for word in tokens if not word in stopwords.words("english")]
    
    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    # iterate through each token
    clean_tokens = []
    for tok in tokens:
        
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens 
    
    pass


def build_model():
    
    '''  Builds a pipeline model
    
    OUTPUT:
    model_pipeline - A pipeline-based model with the following characteristics:
            - makes use of "CountVectorizer" as vectorizer
            - makes use of "TfidfTransformer" as transformer
            - makes use of "MultiOutputClassifier", subtype "RandomForestClassifier", as classifier
            - makes use of GridSearchCV in order to find the optimal combination of differemt hyperparameters
    
    '''
    
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(KNeighborsClassifier()))   
    ])
    
    parameters = {
       'vect__ngram_range': [(1, 1)],
       'vect__max_df': [0.5],
       'vect__max_features': [None],
       'clf__estimator__n_neighbors': [2]
                 } 
    
    
    model_pipeline = GridSearchCV(pipeline, parameters)
    
    return model_pipeline
 

def train(X_train, y_train, model):
    
    ''' Fits the model with the train components of X and Y
    
    INPUT:
    X_train - train component of the dataframe corresponding to the attribute variable
    y_train - train component of the dataframe corresponding to the target variable
    model - mathematical model that will be fitted with the train components of attribute variable X and target attribute y
   
    OUTPUT:
    model - mathematical model that was inserted as input of the function, already fitted with X_test and y_test   
   
    '''

    # fit model
    model.fit(X_train, y_train)
    
    return model



def evaluate_model(model, X_test, y_test, category_names):    
    
    ''' Evaluates the model, providing the test_score by using ClassificationReport (useful for multi-target models)
    
    INPUT:
    model - mathematical model that was already fitted with X_test and y_test in the train function 
    X_test - dataframe that corresponds to the train component of the attribute variable X
    y_test - contains the train component of the target variable yy - dataframe corresponding to the target variable; will be divided into train ant test sets
 
   
    '''    
    
    y_test_pred = model.predict(X_test)

    # y_test_pred and y_train_pred are obtaines as numpy arrays
    # for further operations, we need to convert them into dataframe
    # therefore, y_test_pred_df and y_train_pred_df are introduced:

    y_headers = y_test.columns

    y_test_pred_df = pd.DataFrame(y_test_pred, columns = y_headers)

    
    for col in y_test:
        test_score = classification_report(y_test[col],y_test_pred_df[col],)
        print(test_score)
        


def save_model(model, model_filepath):
    
    ''' Saves the model as a pickle file
    
    INPUT:
    model - mathematical model that was already fitted with X_test and y_test in the train function 
    model_filepath - path where model will be saved
   
    '''       
    
    pkl_filename = '{}'.format(model_filepath)
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


def main():
    
    ''' Performs a series of operations to build a pipeline-based model fitted and tested with information contained in the database file contained in database_filepath,
        evaluates the model and stores the model in the path defined by model_filepath
    
    INPUT:
    database_filepath - path of the .db file (database) created and stored by the process_data.py script 
    model_filepath - path where model will be saved

    '''
    
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()