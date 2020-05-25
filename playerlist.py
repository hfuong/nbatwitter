# Import relevant modules
import requests

# Get web page
site = requests.get("https://stats.nba.com/players/list/")

# Print status code; 200 = successfully downloaded
print(site)

