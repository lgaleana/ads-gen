import pytest
from scripts.url_text_extractor import extract_text_from_url, extract_images_from_url
from unittest.mock import patch


def test_extract_text_from_url():
    url = 'http://example.com'
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.text = '<html><body>Example Domain</body></html>'
        extract_text_from_url(url)
        mocked_get.assert_called_with(url)


def test_extract_images_from_url():
    url = 'http://example.com'
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.text = '<html><body><img src="example.jpg"></body></html>'
        extract_images_from_url(url)
        mocked_get.assert_called_with(url)