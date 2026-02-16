# Import needed libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests, time, datetime,re, random

# Headers variable temporary, will delete later
headers  = {'User-Agent': 'insert your headers here'}


# Use to produce random delays during mass-scraping, ensures we are not overwhelming a site
# Random delay function to not overwhelm the site
def perform_random_delay(delay = 3, random_offset = 0.5):
    time.sleep(delay + random.uniform(0, random_offset))



# Obtain a list of links for one page
def scrape_backloggd_game_links(page_link: str, headers=headers):
    
    # Request the page's contents
    req = requests.get(page_link, headers=headers)
    if req.status_code != 200:
        print("FAILED")
        return []
    
    # Create a soup instance to easily access the page
    soup = BeautifulSoup(req.text, 'html.parser')

    # Get the game links, store in an array
    games_on_page = soup.find_all("a", class_ = "cover-link", href=True)

    game_links = []
    for game in games_on_page:
        game_links.append("https://backloggd.com" + game["href"])
        perform_random_delay()
    
    # Return the final array
    return game_links
