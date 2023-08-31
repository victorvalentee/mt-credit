import sqlite3

def initialize_database():
    # Initialize the database connection
    db_conn = sqlite3.connect('../database/credit_cards.db')
    db_cursor = db_conn.cursor()

    with open("../database/schema.sql", "r") as schema_file:
        schema_sql = schema_file.read()
        db_conn.executescript(schema_sql)

    # Initialize database with sample data
    initial_rows = [
        ('2055-03-31', 'VAV', '1234567890123456', 123),
        ('2056-04-30', 'ABC', '9876543210987654', 456),
        ('2057-05-31', 'XYZ', '5678901234567890', 789)
    ]

    for row in initial_rows:
        db_cursor.execute("INSERT INTO cards (exp_date, holder_name, card_number, cvv) VALUES (?, ?, ?, ?)", row)

    db_conn.commit()


if __name__ == '__main__':
    initialize_database()