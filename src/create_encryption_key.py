from cryptography.fernet import Fernet
key = Fernet.generate_key()


# Create encryption key and save it to a file
def generate_encryption_key():
    with open('encryption.key', 'wb') as key_file:
        key_file.write(key)


if __name__ == '__main__':
    generate_encryption_key()
