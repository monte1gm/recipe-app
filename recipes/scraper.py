# recipes/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string.strip() if soup.title else 'No Title'

    # Very generic ingredient and instruction scrapers (to be customized)
    ingredients = [li.get_text(strip=True) for li in soup.select("li") if 'ingredient' in li.get('class', [])]
    steps = [p.get_text(strip=True) for p in soup.find_all("p") if 'step' in p.get('class', [])]

    return {
        "title": title,
        "ingredients": ingredients,
        "steps": steps
    }
