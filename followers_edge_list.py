# Import relevant packages
import pandas as pd

# Load data
df = pd.read_csv('data/followers.csv', index_col = 0)
players = pd.read_csv('data/currenttwitter_updated.csv')

# Remove rows where neither player follows each other (i.e., remove False & False but keep any with True)
df = df[df['following_user2'] | df['following_user1']]

# Add player names to match screen names
df = df.merge(players.rename(columns = {'handle': 'user1_name', 'currentplayer': 'user1_player'}),
              on = 'user1_name', how = 'left')

df = df.merge(players.rename(columns = {'handle': 'user2_name', 'currentplayer': 'user2_player'}),
              on = 'user2_name', how = 'left')

# Re-order columns, remove screen names
df = df[['user1_player', 'following_user2', 'user2_player', 'following_user1']]

print(df)
