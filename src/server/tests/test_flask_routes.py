import pytest
from server.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_store_credit_card(client):
    data = {
        'exp_date': '2023-12-31',
        'holder_name': 'John Doe',
        'card_number': '1234567890123456',
        'cvv': 123
    }

    response = client.post('/api/v1/credit-card', json=data)
    assert response.status_code == 201
    assert response.json == {'message': 'Credit card stored successfully'}