from utils import aes_encrypt

def get_all_cards(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM cards")
    cards_list = cursor.fetchall()

    # Remove encrypted byte-string from results
    result = [(row[:-1]) for row in cards_list]
    return result


# Function to retrieve a card by encrypted card number
def get_card_by_number(db_conn, card_number):
    # Encrypt the card_number deterministically
    encrypted_search_value = aes_encrypt(card_number)

    cursor = db_conn.cursor()
    cursor.execute(f"SELECT exp_date, holder_name, card_number, cvv FROM cards WHERE card_number_encrypted = ?", (encrypted_search_value,))
    card_details = cursor.fetchall()

    return card_details


def create_credit_card(db_conn, credit_card_info: dict):
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO cards (exp_date, holder_name, card_number, cvv, card_number_encrypted) VALUES (?, ?, ?, ?, ?)",
        (credit_card_info['exp_date'], credit_card_info['holder_name'], credit_card_info['card_number'], credit_card_info['cvv'], credit_card_info['card_number_encrypted'])
    )
    
    cursor.execute(f"""
        SELECT * FROM cards 
        WHERE card_number = '{credit_card_info['card_number']}'
            AND holder_name = '{credit_card_info['holder_name']}'
    """)
    
    return cursor.fetchall()
