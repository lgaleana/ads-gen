import pytest
from scraper import scrape


def test_scrape():
    url = 'http://example.com'
    text, images = scrape(url)
    assert text is not None
    assert images is not None