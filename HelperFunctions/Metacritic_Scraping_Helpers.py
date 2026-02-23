# Import needed libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests, time, datetime,re, random

# Headers variable temporary, will delete later
headers  = {'User-Agent': 'insert your user agent here'}

def scrape_metacritic_page(page_link:str, heders=headers):
    req = requests.get(page_link, headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    print(req.text)

    # Get meta score + rating count
    meta_score = soup.find("div", attrs = {"data-testid": "critic-score-info"}).find("div", class_ = "c-productScoreInfo_scoreNumber u-float-right").find("span").text
    meta_rating_count = soup.find("div", attrs = {"data-testid": "critic-score-info"}).find("span", class_ = "c-productScoreInfo_reviewsTotal u-block").find("span").text
    meta_rating_count = meta_rating_count.split(" ")[2].replace(",", "")

    # Get user score + rating count
    user_score = soup.find("div", attrs = {"data-testid": "user-score-info"}).find("div", class_ = "c-productScoreInfo_scoreNumber u-float-right").find("span").text
    user_rating_count = soup.find("div", attrs = {"data-testid": "user-score-info"}).find("span", class_ = "c-productScoreInfo_reviewsTotal u-block").find("span").text
    user_rating_count = user_rating_count.split(" ")[2].replace(",", "")

    # Getting genre, publisher, and developer
    game_details = soup.find("div", attrs={"data-testid":"details-game"}).find("div", class_="c-productionDetailsGame_grid u-grid").find("div", class_ = "c-gameDetails")
    genre = game_details.find("div", class_ = "c-gameDetails_sectionContainer u-flexbox u-flexbox-row u-flexbox-alignBaseline").find("span", class_ = "c-globalButton_label").text
    developer = game_details.find("div", class_ = "c-gameDetails_Developer u-flexbox u-flexbox-row").find("a").text
    publisher = game_details.find("div", class_ = "c-gameDetails_Distributor u-flexbox u-flexbox-row").find("a").text

    # Return as a dictionary
    return {'Meta Score': meta_score, 'Number of Critic Ratings': meta_rating_count, 'User Score':user_score,
            'Number of User Rarings': user_rating_count, 'Game Genre': genre, "Game Developer": developer, "Game Publisher": publisher}