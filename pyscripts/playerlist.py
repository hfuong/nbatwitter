# Import relevant modules
import requests
from bs4 import BeautifulSoup


# Get web page
site = requests.get("https://stats.nba.com/players/list/")

# Print status code; 200 = successfully downloaded
print(site)

# Make BeautifulSoup object
page = BeautifulSoup(site.content, features = "lxml")

# Print HTML content with nice formatting
# print(page.prettify())


# Identify the specific page with player names and Twitter accounts
playerTable = page.find('ul', {"class": "players-list__names"})

# Find all instances of player name by beginning of link within the table
playerNameLinks = playerTable.select('a[href^="/players/"]')

print(playerNameLinks)

# Make a list of player names using the text from links
player = []

for name in playerNameLinks:
    player.append(name.text)

print(player)
