"""
This test set is responsible for ensuring
API functions work as expected
"""

import pytest
import sqlite3
from api_functions import get_all_cards, get_card_by_id


# Fixture to set up an in-memory test database
@pytest.fixture
def test_db():
    conn = sqlite3.connect(':memory:')

    with open("../database/schema.sql", "r") as schema_file:
        schema_sql = schema_file.read()
        conn.executescript(schema_sql)

        conn.execute(
            """
                INSERT INTO cards (exp_date, holder_name, card_number, cvv)
                VALUES
                    ('2099-04-01', 'VVV', '123abc', 123),
                    ('2099-04-15', 'Victor Valente', '123abc456', 777);
            """
        )

    conn.commit()
    yield conn
    conn.close()


def test_list_all_cards(test_db):
    actual_result = get_all_cards(test_db)
    expected_result = [
        ('2099-04-30', 'VVV', '123abc', 123), 
        ('2099-04-30', 'Victor Valente', '123abc456', 777)
    ]

    assert actual_result == expected_result


def test_get_card_by_id(test_db):
    actual_result = get_card_by_id(test_db, id="123abc456")
    expected_result = [('2099-04-30', 'Victor Valente', '123abc456', 777)]

    assert actual_result == expected_result
