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
    
    # Return the final array
    return game_links

# Extract all needed information from one backloggd page
def scrape_backloggd_page(page_link:str, headers=headers):
    
    # Get the page's contents
    req = requests.get(page_link, headers=headers)
    if req.status_code != 200:
        print("FAILED")
        return {}
    
    soup = BeautifulSoup(req.text, 'html.parser')
    
    # Get the average rating
    avg_rating =  soup.find("div", class_ ="container backloggd-container center-container h-100").find("h1").text

    # Get the number of ratings
    num_ratings = soup.find("div", class_ = "backloggd-container center-container log-counters h-100").find_all("p", class_ = "mb-0 log-counter-stat")[4].text

    # Get the average playimr
    avg_playtime = soup.find("div", class_ = "backloggd-container center-container theme-pink sm-container h-100").find("p", "mb-0 stat-value element-revealed").text

    # Get the release date
    release_date = soup.find("div", class_ = "container backloggd-container sm-container").find("a").text

    # Platforms can include multiple consoles, so we need to iterate through all the results
    platforms_html = soup.find("div", class_ = "col ml-auto text-right text-md-left").find_all("a")
    platforms = []
    for item in platforms_html:
        platforms.append(item.text)

    return {'Average Backloggd Rating': avg_rating, 'Number of Backloggd Ratings': num_ratings, 'Average Backloggd Playime':avg_playtime,
            'Release Date': release_date, 'Platforms': platforms}
