# Import relevant modules
import requests
from bs4 import BeautifulSoup
import csv


# Get web page
site = requests.get("https://www.basketball-reference.com/friv/twitter.html")

# Print status code; 200 = successfully downloaded
print(site)

# Make BeautifulSoup object
page = BeautifulSoup(site.content, features = "lxml")

# Print HTML content with nice formatting
# print(page.prettify())


# Identify the table with player names and Twitter accounts
playerTable = page.find('table')

# Find all instances of player name by beginning of link within the table
playerNameLinks = playerTable.select('a[href^="/players/"]')

# Find all instances of Twitter handles that contain twitter.com within the table
playerTwitterLinks = playerTable.select('a[href*="twitter.com/"]')

# Make a list of player names and another list of Twitter handles using the text from links
player = []
handle = []

for name in playerNameLinks:
    player.append(name.text)

for account in playerTwitterLinks:
    handle.append(account.text)

# Combine the two lists into a dictionary
nbaTwitter = dict(zip(player, handle))

print(nbaTwitter)

# Print output to CSV
with open('twitterhandles.csv', 'w', encoding = 'utf-8', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['player', 'handle'])
    for key, value in nbaTwitter.items():
        writer.writerow([key, value])
