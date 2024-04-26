import pytest
from bs4 import BeautifulSoup
from scripts.url_text_extractor import extract_text_from_soup, extract_images_from_soup
from unittest.mock import patch


def test_extract_text_from_soup():
    soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    extract_text_from_soup(soup)


def test_extract_images_from_soup():
    soup = BeautifulSoup('<html><body><img src="example.jpg"></body></html>', 'html.parser')
    extract_images_from_soup(soup)