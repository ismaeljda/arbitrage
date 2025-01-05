from bs4 import BeautifulSoup 
import pandas as pd

def extract_matches_betfirst(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    match_data = []
    
    # Trouver tous les matchs
    matches = soup.find_all('div', class_='rj-ev-list__ev-card')
    
    for match in matches:
        try:
            match_info = {}
            
            # Extraire les équipes
            teams = match.find_all('span', class_='rj-ev-list__name-text')
            if len(teams) >= 2:
                match_info['Home_Team'] = teams[0].text.strip()
                match_info['Away_Team'] = teams[1].text.strip()
            
            # Extraire les cotes
            odds = match.find_all('span', class_='rj-ev-list__bet-btn__odd')
            if len(odds) >= 2:
                match_info['Home_Odds'] = float(odds[0].text.strip())
                match_info['Away_Odds'] = float(odds[1].text.strip())
                
            # Ajouter le match seulement si on a toutes les infos
            if len(match_info) == 4:
                match_data.append(match_info)
                
        except Exception as e:
            print(f"Erreur lors de l'extraction d'un match: {e}")
            continue

    df = pd.DataFrame(match_data)
    
    return df