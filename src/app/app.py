from flask import Flask, jsonify, request
from utils import initialize_database
import api_functions
import sqlite3


app = Flask(__name__)

# Route to list all credit cards
@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    with sqlite3.connect('../database/credit_cards.db') as db_conn:
        credit_cards = jsonify(api_functions.get_all_cards(db_conn))
    return credit_cards


# Route to get credit card by id
@app.route('/api/v1/credit-card/<card_number>', methods=['GET'])
def get_credit_card(card_number):
    with sqlite3.connect('../database/credit_cards.db') as db_conn:
        credit_card = jsonify(api_functions.get_card_by_id(db_conn, id=card_number))
    return credit_card or jsonify({'message': 'Credit card not found'}), 404


# Route to create new credit card
@app.route('/api/v1/credit-card', methods=['POST'])
def store_credit_card():
    data = request.json

    with sqlite3.connect('../database/credit_cards.db') as db_conn:
        api_functions.create_credit_card(db_conn, credit_card_info=dict(data))
    return jsonify({'message': 'Credit card stored successfully'}), 201


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)