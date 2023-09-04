from collections import OrderedDict
import json
from flask import Flask, jsonify, request
from utils import get_card_number_encrypted, get_obfuscated_card_number, initialize_database
import api_functions
import sqlite3
from creditcard import CreditCard
from utils import DATABASE_PATH


app = Flask(__name__)
initialize_database()


# Route to list all credit cards
@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    with sqlite3.connect(DATABASE_PATH) as db_conn:
        credit_cards = jsonify(api_functions.get_all_cards(db_conn))
    return credit_cards


# Route to get credit card by id
@app.route('/api/v1/credit-card/<card_number>', methods=['GET'])
def get_credit_card(card_number):
    with sqlite3.connect(DATABASE_PATH) as db_conn:
        credit_card = jsonify(api_functions.get_card_by_id(db_conn, id=card_number))
    return credit_card or jsonify({'message': 'Credit card not found'}), 404


# Route to create new credit card
@app.route('/api/v1/credit-card', methods=['POST'])
def store_credit_card():
    data = request.json

    credit_card_info = data
    card_number_encrypted = get_card_number_encrypted(credit_card_info['card_number'])

    card_number = credit_card_info['card_number']
    
    if CreditCard(card_number).is_valid():
        with sqlite3.connect(DATABASE_PATH) as db_conn:
            # Retains only the last 4 digits of the credit card number
            credit_card_info['card_number'] = get_obfuscated_card_number(card_number)
            credit_card_info['card_number_encrypted'] = card_number_encrypted

            api_functions.create_credit_card(db_conn, credit_card_info=credit_card_info)
        return jsonify({'message': 'Credit card stored successfully'}), 201
    else:
        return jsonify({'message': 'Credit card number is not valid'}), 400




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)