import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import app, run_ollama_chat

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index_route(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b'data-model="deepseek-coder:1.3b-instruct-q2_K"' in response.data

def test_get_response_route(client: FlaskClient, mocker):
    mocker.patch('app.run_ollama_chat', return_value='mocked response')
    
    response = client.post('/get_response', json={'user_input': 'Hello, AI!'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['response'] == 'mocked response'
