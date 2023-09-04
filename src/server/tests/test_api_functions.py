"""
This test set is responsible for ensuring
API functions work as expected
"""

import pytest
import sqlite3
from api_functions import get_all_cards, get_card_by_number, create_credit_card
from utils import aes_encrypt, get_obfuscated_card_number
from utils import DATABASE_SCHEMA_PATH


card_number = '1234567891123456'
encrypted_card_number = aes_encrypt(card_number)
sample_data = ('2055-12-31', 'VAV', get_obfuscated_card_number(card_number), 123, encrypted_card_number)


# Fixture to set up an in-memory test database
@pytest.fixture
def test_db():
    db_conn = sqlite3.connect(':memory:')
    db_cursor = db_conn.cursor()

    with open(DATABASE_SCHEMA_PATH, "r") as schema_file:
        schema_sql = schema_file.read()
        db_conn.executescript(schema_sql)

        # Initialize database with sample data
        db_cursor.execute("INSERT INTO cards (exp_date, holder_name, card_number, cvv, card_number_encrypted) VALUES (?, ?, ?, ?, ?)", sample_data)
        db_conn.commit()

    yield db_conn
    db_conn.close()


def test_list_all_cards(test_db):
    actual_result = get_all_cards(test_db)
    expected_result = [sample_data[:-1]]    

    assert actual_result == expected_result


def test_get_card_by_number(test_db):
    actual_result = get_card_by_number(test_db, card_number)
    expected_result = [sample_data[:-1]]

    assert actual_result == expected_result


def test_create_credit_card(test_db):
    credit_card_info = {
        "exp_date": "2099-04-30",
        "holder_name": "VAV",
        "card_number": "4111111111111111",
        'cvv': 777,
        'card_number_encrypted': None
    }

    actual_result = create_credit_card(test_db, credit_card_info)
    expected_result = [('2099-04-30', 'VAV', '4111111111111111', 777, None)]
   
    assert actual_result == expected_result
