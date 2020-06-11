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
    # Scroll bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Pause scrolling to allow page to load
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source

# Close browser window at end of session
driver.quit()

# Make BeautifulSoup object
page = BeautifulSoup(html, features = "lxml")


# Identify the specific sections with player names
playerParagraph = page.find_all('p', class_='nba-player-index__name')

# Get only the text within the paragraph tags
for p in playerParagraph:
    print(p.get_text(strip = True, separator = ' '))
