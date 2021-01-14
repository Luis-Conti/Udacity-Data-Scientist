import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine
from langdetect import detect
import time

app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')  # engine = create_engine('sqlite:///../data/YourDatabaseName.db')
df = pd.read_sql_table('DisasterResponseTable', engine)                  # df = pd.read_sql_table('YourTableName', engine)


# Dictionary constructed from languages and abbreviations contained in ISO 639-1
lang_dict = { "af": "Afrikaans", "ga": "Irish", "sq": "Albanian",
             "it": "Italian", "ar": "Arabic", "ja": "Japanese",
             "az": "Azerbaijani", "kn": "Kannada", "eu": "Basque",
             "ko": "Korean", "bn": "Bengali", "la": "Latin", 
             "be": "Belarusian", "lv": "Latvian", "bg": "Bulgarian",
             "lt": "Lituanian", "ca": "Catalan", "mk": "Macedonian",
             "zh-CN": "Chinese Simplified", "ms": "Malay",
             "zh-TW": "Chinese Traditional", "mt": "Maltese",
             "hr": "Croatian", "no": "Norwegian", "cs": "Czech", 
             "fa": "Persian", "da": "Danish", "pl": "Polish",  
             "nl": "Dutch", "pt": "Portuguese",  "en": "English",
             "ro": "Romanian", "eo": "Esperanto", "ro": "Romanian",
             "ru": "Russian", "et": "Estonian", "sr": "Serbian",
             "tl": "Filipino", "sk": "Slovak", "fi": "Finnish",
             "sl": "Eslovenian", "fr": "French", "es": "Spanish",
             "gl": "Galician", "sw": "Swahili", "ka": "Georgian",
             "sv": "Swedish", "de": "German", "ta": "Tamil",
             "el": "Greek", "te": "Telugu", "gu": "Gujarati",
             "th": "Thai", "ht": "Haitian Creole", "tr": "Turkish",
             "iw": "Hebrew", "uk": "Ukrainian", "hi": "Hindi",
             "ur": "Urdu", "hu": "Hungarian", "vi": "Vietnamese",
             "is": "Icelandic", "cy": "Welsh", "id": "Indonesian",
             "yi": "Yiddish", "co": "Corsican", "fy": "Frisian",
             "gd": "Scottish Gaelic", "ha": "Hausa", "haw": "Hawaiian",
             "lb": "Luxembourgish", "mg": "Malagasy", "mr": "Marathi",
             "ny": "Chichewa", "sm": "Samoan", "sn": "Shona",
             "zu": "Zulu", "so": "Somali"}


# Obtain the language corresponding to the original messages
# Note: For thosw rows in with the content of the "original" column is empty, NaN or None, no translation is possible
languages_detected = []


for x in range(len(df["original"])):
    
    if (type(df.loc[x,"original"]) == str):
    
        try:
            languages_detected.append(detect(df.loc[x,"original"]))                   
        except Exception as e:
            print(str(e))
        continue

    

# Convert the result in a dataframe
languages_detected_df = pd.DataFrame(languages_detected)


# Change name of columns in a df
languages_detected_df.rename(columns={0:'Language'}, inplace=True)


# We will get the number of messages per language
# the name of the resulting column will be renamed as "Number of messages"
x_plot =pd.DataFrame(languages_detected_df["Language"].value_counts().sort_values(ascending=False))
x_plot.rename(columns={'Language': 'Number of messages'}, inplace=True)

# Name of rows will also be changed, in order to make it easier to identify the language
x_plot.rename(index= lang_dict , inplace=True)

# Obtain a list of languages, ordered by frequency
Languages_index = pd.DataFrame(list(x_plot.index))
Languages_index[0].replace(lang_dict,inplace=True)

# Obtain a dataframe with two columns: first, the language; second, the genre
df_copy = df.copy()
df_copy = pd.concat([df_copy, languages_detected_df],axis=1)
df_genre_lang = pd.concat([df_copy["genre"],df_copy["Language"]],axis=1)
df_genre_lang["Language"].replace(lang_dict, inplace=True)

# Drop all the NaN
df_genre_lang.dropna(axis=0)

# Create a new table whose rows are the different languages, and the columns the different values of the categorical variable "genre"
# Fill the NaN with 0, if any
df_genre_lang_grouped = df_genre_lang.groupby(['Language'])["genre"].value_counts().unstack()
df_genre_lang_grouped.fillna(0, inplace = True)

# Reorder the rows of the table
parameters = Languages_index[0].tolist()
df_genre_lang_grouped = df_genre_lang_grouped.loc[parameters,:]

# Keep only first 6 rows
df_genre_lang_grouped = df_genre_lang_grouped.iloc[:6]


# load model
model = joblib.load("../models/classifier.pkl")  #model = joblib.load("../models/your_model_name.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    genre_percentages = round(100*genre_counts/genre_counts.sum(), 2)
    
    category_counts = df.drop(['id', 'message', 'original', 'genre'], axis = 1).sum()
    category_counts = category_counts.sort_values(ascending = False)
    category_names = list(category_counts.index)
    
    language_counts = df_genre_lang.groupby('Language').count()["genre"].sort_values(ascending=False)
    language_names = list(language_counts.index)
    
    language_counts_genre_direct = df_genre_lang_grouped["direct"]
    language_counts_genre_social = df_genre_lang_grouped["social"]
    genre_lang_names=list(df_genre_lang_grouped.index)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            "data": [
              {
                "type": "pie",
                "uid": "f4de1f",
                "hole": 0.3,
                "name": "Genre",
                "pull": 0,
                "domain": {
                  "x": genre_percentages,
                  "y": genre_names
                },
                "marker": {
                  "colors": [
                    "#yellow",
                    "#red",
                    "#blue"
                   ]
                },
                "textinfo": "label+value",
                "hoverinfo": "all",
                "labels": genre_names,
                "values": genre_percentages
              }
            ],

            'layout': {
                'title': 'Messages sent per language',
                'yaxis': {
                    'title': "Number of messages"
                },
                'xaxis': {
                    'title': "Language",
                    'tickangle': -90
                }
            }
        }
        
 , {
            'data': [
                Bar(
                    x=category_names,
                    y=category_counts
                )
            ],

            'layout': {
                'title': 'Messages sent per category',
                'yaxis': {
                    'title': "Number of messages"
                },
                'xaxis': {
                    'title': "\n\n\n\nCategory",
                    'tickangle': -90
                }
            }
        }      
        
 , {
            'data': [
                Bar(
                    x=genre_lang_names,
                    y=language_counts_genre_direct,
                    name='Genre: Direct'
                ),
                Bar(
                    x=genre_lang_names,
                    y=language_counts_genre_social,
                    name='Genre: Social',
                )
            ],

            'layout': {
                'title': 'Messages sent per language and genre',
                'yaxis': {
                    'title': "Number of messages"
                },
                'xaxis': {
                    'title': "Language",
                    'tickangle': 0
                },
                'barmode' : 'group'
            }
        }         
                       
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()