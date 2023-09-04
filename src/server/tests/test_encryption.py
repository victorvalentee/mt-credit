from utils import encrypt, decrypt


def test_encryption_key():
    # Encrypt a credit card number
    credit_card_number = "4111111111111111"
    encrypted_number = encrypt(credit_card_number)

    # Decrypt a credit card number
    decrypted_number = decrypt(encrypted_number)