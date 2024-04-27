import pytest
from bs4 import BeautifulSoup
from app.url_text_extractor import extract_text_from_soup, extract_images_from_soup, extract, Url
from unittest.mock import patch
import requests

def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    assert extract_text_from_soup(soup) == 'Example Domain'

def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    assert extract_images_from_soup(soup) == ['example.jpg']

@patch('requests.get')
def test_extract(mock_get):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><body>Example Domain <img src="example.jpg"></body></html>'
    mock_get.return_value = mock_response

    url = {'url': 'http://example.com'}
    result = extract(url)
    assert isinstance(result, dict)
    assert 'text' in result and 'Example Domain' in result['text']
    assert 'images' in result and result['images'] == ['example.jpg']