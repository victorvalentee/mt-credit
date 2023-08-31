import pytest
from server.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_store_credit_card(client):
    data = {
        'exp_date': '2088-12-31',
        'holder_name': 'John Doe',
        'card_number': '8884567890123456',
        'cvv': 123
    }

    response = client.post('/api/v1/credit-card', json=data)
    assert response.json == {'message': 'Credit card stored successfully'}


def test_get_credit_card(client):
    # Simulate a stored credit card
    stored_card = [["2055-04-30", "VAV", "1234567890123456", 123]]

    # Test the route by sending a GET request
    response = client.get('/api/v1/credit-card/1234567890123456')
    assert response.json == stored_card
