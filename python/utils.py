from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_page_html():
    # Configuration de Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Accéder à la page
        url = "https://www.ladbrokes.be/en/sports/#!/basket/us-nba/"
        driver.get(url)
        
        # Attendre que la page charge (ajustez si nécessaire)
        time.sleep(5)
        
        # Récupérer le HTML
        html = driver.page_source
        
        # Parser avec BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Sauvegarder le HTML dans un fichier pour inspection
        with open('page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
            
        print("HTML sauvegardé dans 'page.html'")
        
        return soup
        
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
        return None
        
    finally:
        driver.quit()

if __name__ == "__main__":
    soup = get_page_html()