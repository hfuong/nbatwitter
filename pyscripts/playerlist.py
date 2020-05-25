# Import relevant modules
import requests
import lxml
from bs4 import BeautifulSoup


# Get web page
site = requests.get("https://stats.nba.com/players/list/")

# Print status code; 200 = successfully downloaded
print(site)


# Make BeautifulSoup object
page = BeautifulSoup(site.content, features = "lxml")

# Print HTML content with nice formatting
print(page.prettify())


