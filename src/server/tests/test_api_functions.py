"""
This test set is responsible for ensuring
API functions work as expected
"""

import pytest
import sqlite3
from api_functions import get_all_cards, get_card_by_id, create_credit_card
from utils import DATABASE_SCHEMA_PATH


# Fixture to set up an in-memory test database
@pytest.fixture
def test_db():
    conn = sqlite3.connect(':memory:')

    with open(DATABASE_SCHEMA_PATH, "r") as schema_file:
        schema_sql = schema_file.read()
        conn.executescript(schema_sql)

        conn.execute(
            f"""
                INSERT INTO cards (exp_date, holder_name, card_number, cvv, card_number_encrypted)
                VALUES
                    ('2099-04-01', 'VVV', '123abc', 123, NULL),
                    ('2099-04-15', 'Victor Valente', '123abc456', 777, NULL);
            """
        )

    conn.commit()
    yield conn
    conn.close()


def test_list_all_cards(test_db):
    actual_result = get_all_cards(test_db)
    expected_result = [
        ('2099-04-30', 'VVV', '123abc', 123, None), 
        ('2099-04-30', 'Victor Valente', '123abc456', 777, None)
    ]

    assert actual_result == expected_result


def test_get_card_by_id(test_db):
    actual_result = get_card_by_id(test_db, id="123abc456")
    expected_result = [('2099-04-30', 'Victor Valente', '123abc456', 777, None)]

    assert actual_result == expected_result


def test_create_credit_card(test_db):
    credit_card_info = {
        "exp_date": "2099-04-30",
        "holder_name": "VAV",
        "card_number": "123abc456",
        'cvv': 777,
        'card_number_encrypted': None
    }

    actual_result = create_credit_card(test_db, credit_card_info)
    expected_result = [('2099-04-30', 'VAV', '123abc456', 777, None)]
   
    assert actual_result == expected_result
