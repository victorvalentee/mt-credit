from hashlib import sha256
import sqlite3


DATABASE_PATH = '/src/database/credit_cards.db'
DATABASE_SCHEMA_PATH = '/src/database/schema.sql'


def initialize_database():
    # Initialize the database connection
    with sqlite3.connect(DATABASE_PATH) as db_conn:
        db_cursor = db_conn.cursor()

        with open(DATABASE_SCHEMA_PATH, "r") as schema_file:
            schema_sql = schema_file.read()
            db_conn.executescript(schema_sql)

        # Initialize database with sample data
        initial_rows = [
            ('2055-03-31', 'VAV', get_obfuscated_card_number('1234567890123456'), 123, None),
            ('2056-04-30', 'ABC', get_obfuscated_card_number('9876543210987654'), 456, None),
            ('2057-05-31', 'XYZ', get_obfuscated_card_number('5678901234567890'), 789, None)
        ]

        for row in initial_rows:
            db_cursor.execute("INSERT INTO cards (exp_date, holder_name, card_number, cvv, credit_card_hash) VALUES (?, ?, ?, ?, ?)", row)

        db_conn.commit()


def get_obfuscated_card_number(card_number: str):
    return f'**** **** **** {card_number[-4:]}'


def get_credit_card_hash(credit_card_info: dict):
    credit_card_id = ''.join(str(info) for info in credit_card_info.values())
    credit_card_hash = sha256(credit_card_id.encode()).hexdigest()
    return credit_card_hash


if __name__ == '__main__':
    initialize_database()