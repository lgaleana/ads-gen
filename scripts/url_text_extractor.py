import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for br in soup.find_all("br"):
        br.replace_with(" ")
    text = soup.get_text()
    cleaned_text = ' '.join(text.split())
    print(cleaned_text)

if __name__ == '__main__':
    url = input('Enter the URL: ')
    extract_text_from_url(url)