import betfirst
import unibet
import arbitrage2
import bwin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_page_html(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url) 
    time.sleep(5)
    html = driver.page_source    
    driver.quit()
    return html

def main():
   betfirst_url = "https://betfirst.dhnet.be/en/basketball/united-states-nba/"
   unibet_url = "https://fr.unibetsports.be/betting/sports/filter/basketball/all/matches" 
   bwin_url = "https://www.bwin.be/en/sports/basketball-7/betting/north-america-9/nba-6004"

   betfirst_html = get_page_html(betfirst_url)
   unibet_html = get_page_html(unibet_url)
   bwin_html = get_page_html(bwin_url)

   # Récupérer tous les DataFrames
   dataframes = {
       'Betfirst': betfirst.extract_matches_betfirst(betfirst_html),
       'Unibet': unibet.extract_matches_unibet(unibet_html),
       'Bwin': bwin.extract_moneyline_bwin(bwin_html)
   }

#    for name, df in dataframes.items():
#         if not df.empty:
#             filename = f"{name}_odds_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv"
#             df.to_csv(filename, index=False)
#             print(f"\n{name} : données sauvegardées dans {filename}")
#         else:
#             print(f"\n{name} : aucune donnée à sauvegarder")
   # Comparer chaque paire de bookmakers
   bookmakers = list(dataframes.keys())
   for i in range(len(bookmakers)):
       for j in range(i + 1, len(bookmakers)):
           book1 = bookmakers[i]
           book2 = bookmakers[j]
           print(f"\nAnalyse d'arbitrage entre {book1} et {book2}:")
           arbitrage2.analyze_arbitrage(dataframes[book1], dataframes[book2])

if __name__ == "__main__":
   main()