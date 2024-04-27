import pytest
from bs4 import BeautifulSoup
from app.url_text_extractor import extract_text_from_soup, extract_images_from_soup, extract, Url
from unittest.mock import patch, Mock


def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    assert extract_text_from_soup(soup) == 'Example Domain'


def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    assert extract_images_from_soup(soup) == ['example.jpg']

@patch('app.url_text_extractor.requests.get')
@patch('app.url_text_extractor.Url')
def test_extract(mock_Url, mock_get):
    mock_response = Mock()
    mock_response.text = '<html><body>Example Domain <img src="example.jpg"></body></html>'
    mock_get.return_value = mock_response
    mock_Url.return_value = Url(url='http://example.com')
    result = extract(mock_Url)
    assert 'text' in result
    assert 'images' in result
    assert result['text'] == 'Example Domain'
    assert result['images'] == ['example.jpg']
