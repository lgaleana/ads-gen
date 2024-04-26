import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
from requests.models import Response
from bs4 import BeautifulSoup

@patch('app.main.templates.TemplateResponse')
def test_read_root(mock_template_response):
    mock_template_response.return_value = 'URL Text Extractor'
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert 'URL Text Extractor' in response.text

@patch('requests.get')
@patch('bs4.BeautifulSoup')
def test_extract(mock_bs4, mock_requests_get):
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><body>Example Domain</body></html>'
    mock_requests_get.return_value = mock_response

    mock_soup = BeautifulSoup('<html><body>Example Domain</body></html>', 'html.parser')
    mock_bs4.return_value = mock_soup

    client = TestClient(app)
    response = client.post("/extract", json={"url": "http://example.com"})
    assert response.status_code == 200
    assert "text" in response.json()
    assert "images" in response.json()