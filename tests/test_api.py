import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test de la route racine"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Gemini Chat API is running"}


@patch("app.main.model.generate_content")
def test_chat_success(mock_generate):
    """Test de la route /chat avec succès"""
    # Mock de la réponse de Gemini
    mock_response = MagicMock()
    mock_response.text = "Bonjour ! Comment puis-je vous aider ?"
    mock_generate.return_value = mock_response

    response = client.post("/chat", json={"message": "Hello"})
    
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] == "Bonjour ! Comment puis-je vous aider ?"


@patch("app.main.model.generate_content")
def test_chat_error(mock_generate):
    """Test de la route /chat avec erreur"""
    # Simule une erreur de Gemini
    mock_generate.side_effect = Exception("API Error")

    response = client.post("/chat", json={"message": "Hello"})
    
    assert response.status_code == 500