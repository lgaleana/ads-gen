import requests
from bs4 import BeautifulSoup


def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    images = soup.find_all('img')
    return text, images