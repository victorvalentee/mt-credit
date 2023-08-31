from flask import Flask, jsonify
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


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)