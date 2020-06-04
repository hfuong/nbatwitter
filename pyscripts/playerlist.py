# Import relevant modules
from selenium import webdriver
from bs4 import BeautifulSoup


# Get web page with dynamic content that requires scrolling to load
driver = webdriver.Chrome(executable_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get('https://nba.com/players/')

html = driver.page_source

# Make BeautifulSoup object
page = BeautifulSoup(html)


# Identify the specific page with player names and Twitter accounts
playerTable = page.find_all('p', class_='nba-player-index__name')

print(playerTable)
