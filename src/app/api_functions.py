import sqlite3

def get_all_cards(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM cards")
    card_details = cursor.fetchall()
    db_conn.close()

    return card_details


def get_card_by_id(db_conn, id="123abc456"):
    cursor = db_conn.cursor()
    cursor.execute(f"SELECT * FROM cards WHERE card_number = '{id}'")
    card_details = cursor.fetchall()
    db_conn.close()

    return card_details