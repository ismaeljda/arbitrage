from difflib import SequenceMatcher

def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()

def get_game(game, others_df):
    max_similarity = 0
    best_match = None
    
    # Pour le match à comparer, on concatène les équipes pour faire la comparaison
    game_str = f"{game['Home_Team']} {game['Away_Team']}"
    
    # On parcourt chaque ligne du DataFrame others
    for _, other in others_df.iterrows():
        # On fait la même chose pour l'autre match
        other_str = f"{other['Home_Team']} {other['Away_Team']}"
        
        # Calcul de la similarité
        similarity = str_similarity(game_str, other_str)
        
        # Si on trouve une meilleure correspondance
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = other
    if max_similarity > 0.3:
        print (game_str)
        print(best_match)
        return best_match
    else :
        None
    
def arb2(a, b):
	return (1 - (1/a + 1/b)) * 100

def analyze_arbitrage(df1, df2):
    for index, row1 in df1.iterrows():
        # Trouver le match le plus similaire directement avec row1
        matching_row = get_game(row1, df2)
        
        # Si aucun match correspondant n'est trouvé, passer au suivant
        # if matching_row is None:
        #     print(f"Pas de match trouvé pour {row1['Home_Team']} vs {row1['Away_Team']}.")
        #     continue

        # Calculer et afficher les arbitrages
        try:
            arb1 = arb2(row1['Home_Odds'], matching_row['Away_Odds'])
            arb2_value = arb2(row1['Away_Odds'], matching_row['Home_Odds'])

            print(f"\nMatch: {row1['Home_Team']} vs {row1['Away_Team']}")
            print(f"Match trouvé dans df2: {matching_row['Home_Team']} vs {matching_row['Away_Team']}")
            print(f"Valeurs df1: Home_Odds={row1['Home_Odds']}, Away_Odds={row1['Away_Odds']}")
            print(f"Valeurs df2: Home_Odds={matching_row['Home_Odds']}, Away_Odds={matching_row['Away_Odds']}")
            print(f"Arbitrage Home/Away: {arb1:.2f}%")
            print(f"Arbitrage Away/Home: {arb2_value:.2f}%")
        except KeyError as e:
            print(f"Erreur lors du calcul d'arbitrage pour {row1['Home_Team']} vs {row1['Away_Team']}: {e}")
