import json
from flask import jsonify
import pytest
from server.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_store_credit_card_fail(client):
    data = {
        'exp_date': '2088-12-31',
        'holder_name': 'John Doe',
        'card_number': '8884567890123456',
        'cvv': 123,
        'card_number_encrypted': None
    }

    response = client.post('/api/v1/credit-card', json=data)
    assert response.json == {'message': 'Credit card number is not valid'}


def test_store_credit_card(client):
    data = {
        'exp_date': '2088-12-31',
        'holder_name': 'John Doe',
        'card_number': '4160239414178485',
        'cvv': 123
    }

    response = client.post('/api/v1/credit-card', json=data)
    assert response.json == {'message': 'Credit card stored successfully'}


def test_get_credit_card_not_found(client):
    # Test the route by sending a GET request
    response = client.get('/api/v1/credit-card/**** **** **** 0000')
    assert response.json == {'message': 'Credit card not found'}
