# Import relevant modules
from playerlist import players
from twitterhandles import nbaTwitter
import csv

# Narrow down Twitter handles to only current players
currentTwitter = {}

for player, handle in nbaTwitter.items():
    for current in players:
        if current == player:
            currentTwitter[player] = handle

# Print output to CSV
with open('data/currenttwitter.csv', 'w', encoding = 'utf-8', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['currentplayer', 'handle'])
    for key, value in currentTwitter:
        writer.writerow([key, value])
