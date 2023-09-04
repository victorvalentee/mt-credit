from utils import aes_decrypt, aes_encrypt, get_encryption_key


def test_aes_encryption():
    key = get_encryption_key()
        
    # Encrypt a credit card number
    credit_card_number = "4111111111111111"
    encrypted_number = aes_encrypt(credit_card_number)

    # Decrypt a credit card number
    decrypted_number = aes_decrypt(encrypted_number)

    assert credit_card_number == decrypted_number