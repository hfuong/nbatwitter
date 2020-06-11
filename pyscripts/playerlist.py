# Import relevant modules
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# Get web page with dynamic content that requires scrolling to load
driver = webdriver.Chrome(executable_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get("https://nba.com/players/")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(5)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source

# Close browser window at end of session
driver.quit()

# Make BeautifulSoup object
page = BeautifulSoup(html)


# Identify the specific page with player names and Twitter accounts
playerTable = page.find_all('p', class_='nba-player-index__name')

print(playerTable)
