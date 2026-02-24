# Video Game Data Scraping And Analysis Project Overview 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
This is an ongoing personal project of mine that I am utilizing to expand my knowledge of data analysis, database design, and data analysis tools. The current goal of this project is to scrape data from a few sites that contain information about video games, such as release dates, user and critic ratings, developers, publishers, genres, etc. I will then format this data and export it to a database in PostgreSQL using Apache Airflow to orchestrate the process. I will also be exploring the data to discover trends in player preferences, and creating a few Tableau dashboards to show my discoveries.

The sites that are currently being used to obtain data for this project are Backloggd and Metacritic

Lastly, within this document I will log the amount of progress I have made every 1-2 weeks.

# PROGESS UPDATES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
02/24/2026: Within the past 1.5 weeks, I have explored the game pages for Backloggd and Metacritic and wrote code to scrape data about video games from them. However, Metacritic just updated the HTML for their webpages, which means I will need to rewrite some code to properly scrape it. I have also created helper functions to assist with scraping data from Backloggd. The plan moving forward will be to construct a DataFrame with just data from Backloggd and then use Airflow to construct an inital database in PostgreSQL. During this time, I will be re-writing code for Metacritic and create helper functions for scraping its content too.
