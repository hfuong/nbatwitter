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

# Create two df where columns are follower, following, and True/False, remove screen names
df1 = df[['user1_player', 'user2_player', 'following_user2']]
df2 = df[['user2_player', 'user1_player', 'following_user1']]

# Rename columns
df1.columns = ['user_follower', 'user_following', 'following']
df2.columns = ['user_follower', 'user_following', 'following']

# Concatenate into one dataframe
edgeList = pd.concat([df1, df2], ignore_index = True)

# Remove values where following = False (i.e., include only True values)
edgeList = edgeList[edgeList['following']]

# Remove following column
edgeList = edgeList.drop(columns = ['following'])

# Write edge list to CSV, without index
edgeList.to_csv('data/followers_edgelist.csv', index = False)

# Count number of True values (this value will match final number of rows in edge list)
print('Estimated number of rows:', len(df[df['following_user2']]) + len(df[df['following_user1']]))

# For checking purposes, print length of edge list (should match estimate)
print('Total length of edge list:', len(edgeList))
