import tweepy

auth = tweepy.OAuthHandler('XXX', 'XXX')
auth.set_access_token("XX-XX", 
    "XXX")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
