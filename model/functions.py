import pandas as pd
import re

def clean_tweet(tweet):
    cleaned_tweet = re.sub('@\S+', '', tweet) # Remove mentions
    cleaned_tweet = re.sub('https\S+', '', cleaned_tweet) # Remove urls
    cleaned_tweet = re.sub('\S+…', '', cleaned_tweet) # Remove truncated last word
    cleaned_tweet = re.sub('\n', '', cleaned_tweet)
    cleaned_tweet = re.sub('\t', '', cleaned_tweet)
    
    return cleaned_tweet.strip()

def prepare_data():
    republicans = pd.read_csv('../../data/republican_tweets.csv', index_col='id')
    democrats = pd.read_csv('../../data/democrat_tweets.csv', index_col='id')

    data = republicans.append(democrats)
    
    data = data.loc[~data.index.duplicated(keep='first')]
    data['text'] = data['text'].apply(clean_tweet)
    
    return data