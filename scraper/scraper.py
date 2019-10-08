import tweepy
import pandas as pd

auth = tweepy.OAuthHandler('m0Buhp16DQJgVVH3iUGxtd8xb', '7q6HnOlEnBRfyLnq4amra7eGcsFfEAq5YS3ao85eS8SLr3R6O8')
auth.set_access_token("1179698216071258112-CqXjSp4NbLYgxC0jmZZRWdtb8gWwjk", 
    "93p6a16YhBBtPerW7xJiSYu5pDcwTyYlAPfKKMWPVKAHp")

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