from cryptography.fernet import Fernet
from utils import KEY_FILE_PATH

key = Fernet.generate_key()


# Create encryption key and save it to a file
def generate_encryption_key():
    with open(KEY_FILE_PATH, 'wb') as key_file:
        key_file.write(key)


if __name__ == '__main__':
    generate_encryption_key()
