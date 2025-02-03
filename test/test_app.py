import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import app, run_ollama_chat

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index_route(client: FlaskClient):
    """Test to ensure the index route loads correctly and includes the IAmodel variable."""
    response = client.get('/')
    assert response.status_code == 200
    # Print the HTML content to debug
    print(response.data.decode())
    assert b'Powered by deepseek-coder:1.3b-instruct-q2_K' in response.data, "IAmodel not found in the HTML response"

def test_get_response_route(client: FlaskClient, mocker):
    """
    Test the get_response route by mocking the run_ollama_chat function.
    Ensures that the response contains the mocked message with Markdown formatting.
    """
    mocker.patch('app.run_ollama_chat', return_value={
        "message": "# Welcome to the JSON Example\n\nThis is a sample message formatted using Markdown. Here are some things you can do with Markdown:\n\n- Create headings and subheadings\n- Emphasize text with italics or bold\n- Create lists, like this one\n- Add links, like [this one](https://example.com)\n\nHere's a code snippet example:\n\n```javascript\nconsole.log('Hello, world!');\n```\n\nAnd a quote:\n\n> \"Markdown is awesome!\""
    })
    
    response = client.post('/get_response', json={'user_input': 'Hello, AI!'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['response'] == {
        "message": "# Welcome to the JSON Example\n\nThis is a sample message formatted using Markdown. Here are some things you can do with Markdown:\n\n- Create headings and subheadings\n- Emphasize text with italics or bold\n- Create lists, like this one\n- Add links, like [this one](https://example.com)\n\nHere's a code snippet example:\n\n```javascript\nconsole.log('Hello, world!');\n```\n\nAnd a quote:\n\n> \"Markdown is awesome!\""
    }, "Mocked response does not match"
