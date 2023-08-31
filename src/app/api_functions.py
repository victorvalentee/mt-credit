import sqlite3

def get_all_cards(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM cards")
    card_details = cursor.fetchall()
    db_conn.close()

    return card_details

# Example usage
if __name__ == "__main__":
    all_cards = get_all_cards()
    for card in all_cards:
        print(card)