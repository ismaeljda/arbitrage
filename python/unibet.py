from bs4 import BeautifulSoup
import pandas as pd
def extract_matches_unibet(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    match_data = []
    
    matches = soup.find_all('div', class_='f9aec _0c119 bd9c6')
    
    for match in matches:
        try:
            teams = match.find_all('div', {'data-test-name': 'teamName'})
            equipe_home = teams[0].text.strip()
            equipe_guest = teams[1].text.strip()
            
            odds = match.find_all('span', {'data-test-name': 'odds'})
            cote_home = float(odds[0].text.strip().replace(',', '.'))
            cote_guest = float(odds[1].text.strip().replace(',', '.'))
            
            match_data.append({
                'Home_Team': equipe_home,
                'Away_Team': equipe_guest,
                'Home_Odds': cote_home,
                'Away_Odds': cote_guest
            })
        except Exception as e:
            print(f"Error extracting Unibet match data: {e}")
            continue
    
    return pd.DataFrame(match_data)