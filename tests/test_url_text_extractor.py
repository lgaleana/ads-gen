import pytest
from bs4 import BeautifulSoup
from scripts.url_text_extractor import get_soup_from_url, extract_text_from_soup, extract_images_from_soup
from unittest.mock import patch


def test_get_soup_from_url():
    url = 'http://example.com'
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.text = '<html><body>Example Domain</body></html>'
        get_soup_from_url(url)
        mocked_get.assert_called_with(url)


def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    extract_text_from_soup(soup)


def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    extract_images_from_soup(soup)