# Import relevant modules
import pandas as pd

# Load CSV files
player = pd.read_csv('data/currentplayers.csv')
twitter = pd.read_csv('data/currenttwitter.csv')

# Check that the current players excluded actually do not have Twitter
# i.e. make sure it is not a spelling error between NBA & Basketball Reference
noTwitter = set(player['player']) ^ set(twitter['currentplayer'])

print(noTwitter)

# Some errors relate to exclusion of accents or suffixes in NBA website (vs. Basketball Reference)
