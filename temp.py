import HelperFunctions.Backloggd_Scraping_Helpers as backloggd_helpers
import HelperFunctions.Metacritic_Scraping_Helpers as metacritic_helpers

backloggd_links = backloggd_helpers.scrape_backloggd_game_links("https://backloggd.com/games/lib/popular/")

print(backloggd_links[10])
print(backloggd_helpers.scrape_backloggd_page(backloggd_links[10]))

#mario_odyssey_data = metacritic_helpers.scrape_metacritic_page(page_link="https://www.metacritic.com/game/super-mario-odyssey/")
#print(mario_odyssey_data)