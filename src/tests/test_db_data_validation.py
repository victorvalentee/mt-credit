"""
This test set is responsible for ensuring
in-schema data validation rules are valid
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

    conn.commit()
    yield conn
    conn.close()


def test_account_holder_length_fail(test_db):
    cursor = test_db.cursor()

    with pytest.raises(sqlite3.IntegrityError, match="Account holder name must have at least 3 characters."):
        # Tries to insert invalid holder_name
        cursor.execute(
            """
            INSERT INTO cards (exp_date, holder_name, card_number, cvv)
            VALUES ('2024-04-01', 'VV', '123abc', NULL);
            """
        )


def test_account_holder_length_fail(test_db):     
    cursor = test_db.cursor()
    cursor.execute(
        """
            INSERT INTO cards (exp_date, holder_name, card_number, cvv)
            VALUES ('2024-04-01', 'VVV', '123abc', NULL);
        """
    )

    cursor.execute('SELECT * FROM cards;')
    actual_result = cursor.fetchall()

    expected_result = [('2024-04-30', 'VVV', '123abc', None)]
    assert actual_result == expected_result
