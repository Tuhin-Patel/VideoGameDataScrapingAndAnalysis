import HelperFunctions.BackloggdScraping_Helpers as backloggd_helpers

backloggd_links = backloggd_helpers.scrape_backloggd_game_links("https://backloggd.com/games/lib/popular/")

print(backloggd_links[10])
print(backloggd_helpers.scrape_backloggd_page(backloggd_links[10]))