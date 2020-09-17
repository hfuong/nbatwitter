# Load necessary modules and packages
import os
from dotenv import load_dotenv
import tweepy as tw
import pandas as pd

# Twitter authentication
load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.getenv('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tw.API(auth, wait_on_rate_limit = True)

# Load list of screen names (Twitter handles)
df = pd.read_csv('data/currenttwitter.csv')
screenNames = df.handle.tolist()

# Check if screen name exists
for user in screenNames:
    try:
        u = api.get_user(screen_name = user)
    except tw.error.TweepError as e:
        if e.args[0][0]['code'] == 50:
            print('Screen name that does not exist:', user)

            # Remove from dataframe and print to CSV
            df[~df.handle.str.contains(user)]
            df.to_csv('data/currenttwitter_updated.csv', index = False)
