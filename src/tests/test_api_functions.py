"""
This test set is responsible for ensuring
API functions work as expected
"""

import pytest
import sqlite3


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
                VALUES ('2099-04-01', 'VVV', '123abc', 123);
            """
        )

    conn.commit()
    yield conn
    conn.close()


def test_list_all_cards(test_db):
    actual_result = api_functions.get_all_cards()
    expected_result = [('2099-04-30', 'VVV', '123abc', 123)]

    assert actual_result == expected_result
