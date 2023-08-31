import sqlite3

def get_all_cards(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM cards")
    cards_list = cursor.fetchall()

    return cards_list


def get_card_by_id(db_conn, id="123abc456"):
    cursor = db_conn.cursor()
    cursor.execute(f"SELECT * FROM cards WHERE card_number = '{id}'")
    card_details = cursor.fetchall()

    return card_details


def create_credit_card(db_conn, credit_card_info: dict):
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO cards (exp_date, holder_name, card_number, cvv, credit_card_hash) VALUES (?, ?, ?, ?, ?)",
        (credit_card_info['exp_date'], credit_card_info['holder_name'], credit_card_info['card_number'], credit_card_info['cvv'], credit_card_info['credit_card_hash'])
    )
    
    cursor.execute(f"""
        SELECT * FROM cards 
        WHERE card_number = '{credit_card_info['card_number']}'
            AND holder_name = '{credit_card_info['holder_name']}'
    """)
    
    return cursor.fetchall()
