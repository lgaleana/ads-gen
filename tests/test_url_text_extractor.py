import pytest
from bs4 import BeautifulSoup
from app.url_text_extractor import extract_text_from_soup, extract_images_from_soup
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app


def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    assert extract_text_from_soup(soup) == 'Example Domain'


def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    assert extract_images_from_soup(soup) == ['example.jpg']


def test_extract():
    client = TestClient(app)
    response = client.post('/extract', json={'url': 'https://example.com'})
    assert response.status_code == 200
    assert 'text' in response.json()
    assert 'images' in response.json()