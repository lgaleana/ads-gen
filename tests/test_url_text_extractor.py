import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch, Mock
from app.url_text_extractor import extract_text_from_soup, extract_images_from_soup, extract, Url

def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    assert extract_text_from_soup(soup) == 'Example Domain'

def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    assert extract_images_from_soup(soup) == ['example.jpg']

@patch('app.url_text_extractor.requests.get')
def test_extract(mock_get):
    mock_response = Mock()
    mock_response.text = '<html><body>Example Domain<img src="example.jpg"></body></html>'
    mock_get.return_value = mock_response

    url = Url(url='http://example.com')
    result = extract(url)
    assert isinstance(result, dict)
    assert 'text' in result and result['text'] == 'Example Domain'
    assert 'images' in result and result['images'] == ['example.jpg']