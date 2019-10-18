import tweepy
import pandas as pd

auth = tweepy.OAuthHandler('XXX', 'XXX')
auth.set_access_token("XX-XX", 
    "XXX")

api = tweepy.API(auth, wait_on_rate_limit=True)
tweets = api.search(q="american politics",count=1000, since="2015-01-01")

print(tweets[0]._json.keys())
"""
message,favorite_count,retweet_count,created_at,user_name=[],[],[],[],[]
followers_count = []
for tweet in tweets:
    message.append(tweet.text)
    favorite_count.append(tweet.favorite_count)
    retweet_count.append(tweet.retweet_count)
    created_at.append(tweet.created_at)
    user_name.append(tweet.user.name)
    followers_count.append(tweet.user.followers_count)
    
df=pd.DataFrame({'Message':message,
                'Favourite Count':favorite_count,
                'Retweet Count':retweet_count,
                'Created At':created_at,
                'user_name':user_name})
print(df)
"""
