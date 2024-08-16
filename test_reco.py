from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_client(client):
    resp=client.get('/ping')
    assert resp.status_code==200

def test_reco(client):
    test_data = {"user_input": "data science"}  # Using form data
    resp = client.post('/recommend', data=test_data)  # Use 'data' instead of 'json'
    assert resp.status_code == 200