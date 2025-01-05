from bs4 import BeautifulSoup
import pandas as pd

def extract_moneyline_bwin(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    match_data = []

    # Trouver tous les blocs de matchs
    matches = soup.find_all('div', class_='grid-event-wrapper')
    
    for match in matches:
        try:
            # Extraire les noms des équipes
            team_elements = match.select('.participant-container .participant')
            if len(team_elements) >= 2:
                home_team = team_elements[0].text.strip()
                away_team = team_elements[1].text.strip()
            else:
                print("Équipes non trouvées pour ce match.")
                continue

            # Extraire les cotes Money Line
            # Les cotes Money Line se trouvent dans la dernière colonne des options (habituellement deux options)
            moneyline_elements = match.select('.grid-option-group:last-child .option-value')
            if len(moneyline_elements) >= 2:
                home_ml_odds = float(moneyline_elements[0].text.strip())
                away_ml_odds = float(moneyline_elements[1].text.strip())
            else:
                print("Cotes Money Line non trouvées pour ce match.")
                continue

            # Ajouter les données dans la liste
            match_data.append({
                'Home_Team': home_team,
                'Away_Team': away_team,
                'Home_Odds': home_ml_odds,
                'Away_Odds': away_ml_odds
            })

        except Exception as e:
            print(f"Erreur lors de l'extraction des données du match : {e}")
            continue

    # Convertir en DataFrame pour analyse/export
    df = pd.DataFrame(match_data)
    print(f"Nombre total de matchs extraits : {len(df)}")
    return df
