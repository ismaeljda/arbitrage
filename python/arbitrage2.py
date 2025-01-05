NBA_TEAMS = {
    # Eastern Conference
    # Atlantic Division
    "BOSTON": [
        "Boston Celtics",
        "Celtics",
        "BOS",
        "Boston",
        "Boston C."
    ],
    "BROOKLYN": [
        "Brooklyn Nets",
        "Nets",
        "BKN",
        "Brooklyn",
        "BK Nets"
    ],
    "NEW_YORK": [
        "New York Knicks",
        "Knicks",
        "NYK",
        "NY Knicks",
        "New York"
    ],
    "PHILADELPHIA": [
        "Philadelphia 76ers",
        "76ers",
        "Sixers",
        "PHI",
        "Philadelphia",
        "Phila"
    ],
    "TORONTO": [
        "Toronto Raptors",
        "Raptors",
        "TOR",
        "Toronto",
        "TOR Raptors"
    ],

    # Central Division
    "CHICAGO": [
        "Chicago Bulls",
        "Bulls",
        "CHI",
        "Chicago",
        "CHI Bulls"
    ],
    "CLEVELAND": [
        "Cleveland Cavaliers",
        "Cavaliers",
        "Cavs",
        "CLE",
        "Cleveland"
    ],
    "DETROIT": [
        "Detroit Pistons",
        "Pistons",
        "DET",
        "Detroit",
        "DET Pistons"
    ],
    "INDIANA": [
        "Indiana Pacers",
        "Pacers",
        "IND",
        "Indiana",
        "IND Pacers"
    ],
    "MILWAUKEE": [
        "Milwaukee Bucks",
        "Bucks",
        "MIL",
        "Milwaukee",
        "MIL Bucks"
    ],

    # Southeast Division
    "ATLANTA": [
        "Atlanta Hawks",
        "Hawks",
        "ATL",
        "Atlanta",
        "ATL Hawks"
    ],
    "CHARLOTTE": [
        "Charlotte Hornets",
        "Hornets",
        "CHA",
        "Charlotte",
        "CHA Hornets"
    ],
    "MIAMI": [
        "Miami Heat",
        "Heat",
        "MIA",
        "Miami",
        "MIA Heat"
    ],
    "ORLANDO": [
        "Orlando Magic",
        "Magic",
        "ORL",
        "Orlando",
        "ORL Magic"
    ],
    "WASHINGTON": [
        "Washington Wizards",
        "Wizards",
        "WAS",
        "Washington",
        "WSH",
        "WAS Wizards"
    ],

    # Western Conference
    # Northwest Division
    "DENVER": [
        "Denver Nuggets",
        "Nuggets",
        "DEN",
        "Denver",
        "DEN Nuggets"
    ],
    "MINNESOTA": [
        "Minnesota Timberwolves",
        "Timberwolves",
        "Wolves",
        "MIN",
        "Minnesota",
        "MIN Timberwolves"
    ],
    "OKLAHOMA_CITY": [
        "Oklahoma City Thunder",
        "Thunder",
        "OKC",
        "Oklahoma City",
        "OK City"
    ],
    "PORTLAND": [
        "Portland Trail Blazers",
        "Trail Blazers",
        "Blazers",
        "POR",
        "Portland",
        "POR Trail Blazers"
    ],
    "UTAH": [
        "Utah Jazz",
        "Jazz",
        "UTA",
        "Utah",
        "UTA Jazz"
    ],

    # Pacific Division
    "GOLDEN_STATE": [
        "Golden State Warriors",
        "Warriors",
        "GSW",
        "Golden State",
        "GS Warriors"
    ],
    "LA_CLIPPERS": [
        "Los Angeles Clippers",
        "Clippers",
        "LAC",
        "LA Clippers",
        "L.A. Clippers"
    ],
    "LA_LAKERS": [
        "Los Angeles Lakers",
        "Lakers",
        "LAL",
        "LA Lakers",
        "L.A. Lakers"
    ],
    "PHOENIX": [
        "Phoenix Suns",
        "Suns",
        "PHX",
        "Phoenix",
        "PHX Suns"
    ],
    "SACRAMENTO": [
        "Sacramento Kings",
        "Kings",
        "SAC",
        "Sacramento",
        "SAC Kings"
    ],

    # Southwest Division
    "DALLAS": [
        "Dallas Mavericks",
        "Mavericks",
        "Mavs",
        "DAL",
        "Dallas",
        "DAL Mavericks"
    ],
    "HOUSTON": [
        "Houston Rockets",
        "Rockets",
        "HOU",
        "Houston",
        "HOU Rockets"
    ],
    "MEMPHIS": [
        "Memphis Grizzlies",
        "Grizzlies",
        "MEM",
        "Memphis",
        "MEM Grizzlies"
    ],
    "NEW_ORLEANS": [
        "New Orleans Pelicans",
        "Pelicans",
        "NOP",
        "New Orleans",
        "NO Pelicans"
    ],
    "SAN_ANTONIO": [
        "San Antonio Spurs",
        "Spurs",
        "SAS",
        "San Antonio",
        "SA Spurs"
    ]
}

def get_standardized_team_name(team_name):
    """
    Retourne le nom standardisé d'une équipe NBA à partir de n'importe quelle variante connue
    
    Args:
        team_name (str): Le nom de l'équipe à standardiser
        
    Returns:
        str: Le nom standardisé de l'équipe (premier élément de la liste des variantes)
        None: Si aucune correspondance n'est trouvée
    """
    team_name = team_name.strip().lower()
    
    for key, variants in NBA_TEAMS.items():
        if any(variant.lower() == team_name for variant in variants):
            return variants[0]  # Retourne le nom complet officiel
            
    return None

def are_same_team(team1, team2):
    """
    Vérifie si deux noms d'équipe font référence à la même équipe
    
    Args:
        team1 (str): Premier nom d'équipe
        team2 (str): Second nom d'équipe
        
    Returns:
        bool: True si c'est la même équipe, False sinon
    """
    team1 = team1.strip().lower()
    team2 = team2.strip().lower()
    
    for variants in NBA_TEAMS.values():
        variants_lower = [v.lower() for v in variants]
        if team1 in variants_lower and team2 in variants_lower:
            return True
            
    return False

def get_game(game, others_df):
    """
    Trouve le match correspondant dans others_df en utilisant le dictionnaire NBA_TEAMS
    Retourne le match et un booléen indiquant si les équipes sont inversées
    """
    for _, other in others_df.iterrows():
        # Vérifie l'ordre normal (même ordre d'équipes)
        if are_same_team(game['Home_Team'], other['Home_Team']) and \
           are_same_team(game['Away_Team'], other['Away_Team']):
            return other, False
                
        # Vérifie l'ordre inversé
        if are_same_team(game['Home_Team'], other['Away_Team']) and \
           are_same_team(game['Away_Team'], other['Home_Team']):
            return other, True
    
    return None, False

def arb2(a, b):
	return (1 - (1/a + 1/b)) * 100

def analyze_arbitrage(df1, df2):
    """
    Analyse les opportunités d'arbitrage entre deux DataFrames
    """
    for index, row1 in df1.iterrows():
        matching_row, is_swapped = get_game(row1, df2)
        
        if matching_row is None:
            continue
            
        try:
            if not is_swapped:
                # Cas normal : même ordre d'équipes
                arb1 = arb2(row1['Home_Odds'], matching_row['Away_Odds'])
                arb2_value = arb2(row1['Away_Odds'], matching_row['Home_Odds'])
                
                print(f"\nMatch: {row1['Home_Team']} vs {row1['Away_Team']}")
                print(f"Match trouvé: {matching_row['Home_Team']} vs {matching_row['Away_Team']}")
                print(f"Book 1 - Home: {row1['Home_Odds']}, Away: {row1['Away_Odds']}")
                print(f"Book 2 - Home: {matching_row['Home_Odds']}, Away: {matching_row['Away_Odds']}")
                
            else:
                # Cas inversé : il faut inverser les cotes du deuxième bookmaker
                arb1 = arb2(row1['Home_Odds'], matching_row['Home_Odds'])
                arb2_value = arb2(row1['Away_Odds'], matching_row['Away_Odds'])
                
                print(f"\nMatch: {row1['Home_Team']} vs {row1['Away_Team']}")
                print(f"Match trouvé (inversé): {matching_row['Home_Team']} vs {matching_row['Away_Team']}")
                print(f"Book 1 - Home: {row1['Home_Odds']}, Away: {row1['Away_Odds']}")
                print(f"Book 2 - Home: {matching_row['Home_Odds']}, Away: {matching_row['Away_Odds']}")
                
            print(f"Arbitrage Home/Away: {arb1:.2f}%")
            print(f"Arbitrage Away/Home: {arb2_value:.2f}%")
                
        except (KeyError, TypeError) as e:
            print(f"Erreur lors du calcul d'arbitrage: {e}")
