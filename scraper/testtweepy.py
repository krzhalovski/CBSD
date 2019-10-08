import tweepy

auth = tweepy.OAuthHandler('m0Buhp16DQJgVVH3iUGxtd8xb', '7q6HnOlEnBRfyLnq4amra7eGcsFfEAq5YS3ao85eS8SLr3R6O8')
auth.set_access_token("1179698216071258112-CqXjSp4NbLYgxC0jmZZRWdtb8gWwjk", 
    "93p6a16YhBBtPerW7xJiSYu5pDcwTyYlAPfKKMWPVKAHp")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")