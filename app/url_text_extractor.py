import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from fastapi import Depends

class Url(BaseModel):
    url: str


def extract_text_from_soup(soup: BeautifulSoup):
    text = ' '.join(t.strip() for t in soup.stripped_strings)
    return text


def extract_images_from_soup(soup: BeautifulSoup):
    images = [img['src'] for img in soup.find_all('img')]
    for link in soup.find_all('link', rel='stylesheet'):
        if 'background-image' in link['href']:
            images.append(link['href'])
    return images


def extract(url: Url = Depends()):
    response = requests.get(url.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = extract_text_from_soup(soup)
    images = extract_images_from_soup(soup)
    return {'text': text, 'images': images}