import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

@patch('app.main.templates.TemplateResponse')
def test_read_root(mock_template_response):
    mock_template_response.return_value = 'URL Text Extractor'
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert 'URL Text Extractor' in response.text