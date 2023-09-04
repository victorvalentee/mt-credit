from cryptography.fernet import Fernet
from utils import KEY_FILE_PATH


def test_encryption_key():
    with open(KEY_FILE_PATH, 'rb') as key_file:
        encryption_key = key_file.read()

    cipher_suite = Fernet(encryption_key)
    # Encrypt a credit card number
    credit_card_number = "4111111111111111"
    encrypted_number = cipher_suite.encrypt(credit_card_number.encode())

    # Decrypt a credit card number
    decrypted_number = cipher_suite.decrypt(encrypted_number).decode()