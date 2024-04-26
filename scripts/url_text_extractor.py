import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = ' '.join(t.strip() for t in soup.stripped_strings)
    print(text)


def extract_images_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = [img['src'] for img in soup.find_all('img')]
    for link in soup.find_all('link', rel='stylesheet'):
        if 'background-image' in link['href']:
            images.append(link['href'])
    print(images)

if __name__ == '__main__':
    url = input('Enter the URL: ')
    extract_text_from_url(url)
    extract_images_from_url(url)