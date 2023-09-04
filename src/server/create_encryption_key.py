from utils import KEY_FILE_PATH
import os


def generate_encryption_key():
    # Generate a random 256-bit AES encryption key
    key = os.urandom(32)

    # Store the encryption key locally
    with open(KEY_FILE_PATH, "wb") as key_file:
        key_file.write(key)

if __name__ == '__main__':
    generate_encryption_key()
