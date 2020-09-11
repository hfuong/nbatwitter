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
screenNames = ["RealStevenAdams", "Bam1of1", "aldridge_12", "KyleJamal4", "NickeilAW"]

# Look up friendship details
friend_status = api.show_friendship(source_screen_name = screenNames[0], target_screen_name = screenNames[1])

# Print whether user_0 follows user_1 and whether user_1 follows user_0
print(friend_status[0].following, friend_status[1].following)
