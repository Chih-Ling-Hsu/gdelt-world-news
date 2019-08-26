import json
import os
import pandas as pd
from sentiment_analyzer import *

# lang = en
# exist country code
# add sentiment score

# count of keywords for each country

def load_articles(path):
    with open(path, 'r') as f:
        dic = json.load(f)
    df = pd.DataFrame.from_dict(dic)
    return df

def check_validity(df):
    df.dropna(subset=['country', 'url', 'title', 'language'], axis='index', how='any', inplace=True)
    df = df[df['language'] == "English"]
    df['sourcecountry'] = [_.replace('United States', 'USA').replace('United Kingdom', 'England') for _ in df['sourcecountry']]
    return df

def add_sentiments(df):
    df['sentiment'] = [get_sentiment_scores(_) for _ in df['title']]
    df['pos'] = [_['pos'] for _ in df['sentiment']]
    df['neg'] = [_['neg'] for _ in df['sentiment']]
    df['neu'] = [_['neu'] for _ in df['sentiment']]
    df['compound'] = [_['compound'] for _ in df['sentiment']]
    del df['sentiment']
    return df

def fetch_all_news():
    root_dir = 'data/news'
    data = []
    for fn in os.listdir(root_dir):
        try:
            df = load_articles(os.path.join(root_dir, fn))
            df = check_validity(df)
            df = add_sentiments(df)
            df['keyword'] = fn[:-5]
            data.append(df)
        except:
            pass
    news = pd.concat(data)
    news = news.drop_duplicates(subset=['socialimage', 'sourcecountry'])
    news.to_csv('text.csv', index=None)

fetch_all_news()