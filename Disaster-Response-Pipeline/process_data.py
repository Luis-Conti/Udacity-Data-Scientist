import sys
import re
import requests
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    
    ''' Loads datasets contained in messages_filepath and ategories_filepath, and merges them 
    
    INPUT:
    message_filepath - path of the .csv file (dataset) that contains rows with texts corresponding to messages sent during a disaster 
    categories_filepath - path of the .csv file (dataset) that contains the classification of the messages beforehand described   
    
    OUTPUT:
    df - a dataframe that has the following characteristics:
            - was created after the merge of message and categories datasets 
            - merge was performed taking "id" as column is common
            - duplicate rows were dropped from messages.csv before the merge
            - rows with duplicated "id" were dropped from categories.csv before the merge 

    '''
    
    messages = pd.read_csv(messages_filepath, dtype=str)    
    categories = pd.read_csv(categories_filepath, dtype=str)
    messages.drop_duplicates(inplace=True)
    categories.drop_duplicates(subset='id', keep="first", inplace=True)
    df =  messages.merge(categories, how='inner', on=['id'])  
    
    return df

def clean_data(df):
    
    ''' Cleans the dataframe df
    
    INPUT:
    df - dataframe created as a result of the merge of the messages.csv and categories.csv datasets
    
    OUTPUT:
    df - a new dataframe, product of the following operations performed on the input dataframe:
            - new columns were created for each "categories" value 
            - original "categories" column is dropped
            - headers of the new columns correspond to the differemt values of the "categories" column, but with "-0" and "-1" removed
            - values corresponding to the new columns are only "0" or "1", depending on the values of the "categories" column of the categories.csv dataset

    '''
    
    df_categories = df["categories"].str.split(";",expand=True)
    
    row = df_categories.iloc[1,:]
    
    headers=[]
    
    for i in row:
         i = re.sub("-[01]", "", i)
         headers.append(i)
    
    category_colnames = headers
    
    df_categories.columns = category_colnames
    
    for column in df_categories:
 
        df_categories[column] = df_categories[column].str.replace(".+-","")
    
        df_categories[column] = df_categories[column].astype(int)
        
    df_categories.head()
    
    df = df.drop("categories", axis=1)
    
    df = pd.concat([df, df_categories], axis=1)
    
    return df


def save_data(df, database_filename): 
    
    ''' Saves dataframe in a .db file (database)
    
    INPUT:
    df - dataframe obtained as output of the previous function clean_data function
    database_filename - name of the SQL database where dataframe df will be saved

    '''
    
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisasterResponseTable', engine, index=False)
     


def main():
    
    ''' Merges the data contained in message_filepath and categories_filepath, clean the data and stores the resulting dataframe in a database
    
    INPUT:
    message_filepath - path of the .csv file (dataset) that contains rows with texts corresponding to messages sent during a disaster 
    categories_filepath - path of the .csv file (dataset) that contains the classification of the messages beforehand described
    database_filepath - path of the .db file (database) where the final df (output of the clean_data function) will be saved
    


    '''
    
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
             
        
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()