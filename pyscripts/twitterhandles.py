# Import relevant modules
import requests
from bs4 import BeautifulSoup


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

# Print all names
for link in playerNameLinks:
    print(link.text)

# Find all instances of Twitter handles that contain twitter.com within the table
playerTwitterLinks = playerTable.select('a[href*="twitter.com/"]')

# Print all Twitter handles
for link in playerTwitterLinks:
    print(link.text)
