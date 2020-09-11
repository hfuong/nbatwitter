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

# Create empty results df
results = pd.DataFrame(columns = ['user1_name', 'following_user2', 'user2_name', 'following_user1'])

# Loop to look up friendship details for each possible pair (order does not matter; i.e., no repeats)
for user1 in range(len(screenNames)):
    for user2 in range(user1, len(screenNames)):
        # Skip duplicates where user is being paired with himself
        if screenNames[user2] == screenNames[user1]:
            pass
        else:
            try:
                # Get friendship details
                friend_status = api.show_friendship(source_screen_name = screenNames[user1],
                                                    target_screen_name = screenNames[user2])

                user1_name = friend_status[0].screen_name
                following_user2 = friend_status[0].following
                user2_name = friend_status[1].screen_name
                following_user1 = friend_status[1].following

                # Concatenate to a result dataframe
                pair = [user1_name, following_user2, user2_name, following_user1]

                # Append to results dataframe
                results.loc[len(results)] = pair
            except:
                print(user1, user2)

# Write to CSV
results.to_csv('data/followers.csv')
