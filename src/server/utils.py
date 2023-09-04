import sqlite3
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


KEY_FILE_PATH = './encryption.key'
DATABASE_PATH = './database/credit_cards.db'
DATABASE_SCHEMA_PATH = './database/schema.sql'




# AES encryption function
def aes_encrypt(data: str) -> str:
    key = get_encryption_key()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    encoded_data = data.encode()
    data_padded = padder.update(encoded_data) + padder.finalize()
    ciphertext = encryptor.update(data_padded) + encryptor.finalize()

    return ciphertext

# AES decryption function
def aes_decrypt(ciphertext):
    key = get_encryption_key()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    data_padded = decryptor.update(ciphertext) + decryptor.finalize()
    data = unpadder.update(data_padded) + unpadder.finalize()

    decoded_data = data.decode()

    return decoded_data


def get_encryption_key():
    with open(KEY_FILE_PATH, 'rb') as key_file:
        encryption_key = key_file.read()
    return encryption_key


def initialize_database():
    # Initialize the database connection
    with sqlite3.connect(DATABASE_PATH) as db_conn:
        db_cursor = db_conn.cursor()

        with open(DATABASE_SCHEMA_PATH, "r") as schema_file:
            schema_sql = schema_file.read()
            db_conn.executescript(schema_sql)

        # Initialize database with sample data
        initial_rows = [
            ('2055-03-31', 'VAV', get_obfuscated_card_number('1234567890123456'), 123, aes_encrypt('1234567890123456')),
            ('2056-04-30', 'ABC', get_obfuscated_card_number('9876543210987654'), 456, aes_encrypt('9876543210987654')),
            ('2057-05-31', 'XYZ', get_obfuscated_card_number('5678901234567890'), 789, aes_encrypt('5678901234567890'))
        ]

        for row in initial_rows:
            db_cursor.execute("INSERT INTO cards (exp_date, holder_name, card_number, cvv, card_number_encrypted) VALUES (?, ?, ?, ?, ?)", row)

        db_conn.commit()


def get_obfuscated_card_number(card_number: str):
    return f'**** **** **** {card_number[-4:]}'


if __name__ == '__main__':
    initialize_database()