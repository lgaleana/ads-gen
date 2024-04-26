import pytest
from bs4 import BeautifulSoup
from app.url_text_extractor import extract_text_from_soup, extract_images_from_soup, Url, extract
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import HTTPException


def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    assert extract_text_from_soup(soup) == 'Example Domain'


def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    assert extract_images_from_soup(soup) == ['example.jpg']

@patch('app.url_text_extractor.requests.get')
def test_extract(mock_get):
    mock_get.return_value.text = '<html><body>Example Domain</body></html>'
    with pytest.raises(HTTPException):
        extract('invalid')
    assert extract(Url(url='http://example.com')) == {'text': 'Example Domain', 'images': []}