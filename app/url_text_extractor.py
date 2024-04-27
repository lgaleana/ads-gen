import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from fastapi import HTTPException


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


def extract(url: Url):
    try:
        response = requests.get(url.url)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
    soup = BeautifulSoup(response.text, 'html.parser')
    text = extract_text_from_soup(soup)
    images = extract_images_from_soup(soup)
    return {'text': text, 'images': images}