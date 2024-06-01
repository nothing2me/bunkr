import cryptography
import os
from cryptography.fernet import Fernet


def check_master_key_exists():
    # Planning to do key file encryption and decryption,
    # just need to work out solutions
    keyfile = "encrypted_key.key"
    # Create a new key and keyfile if none was found
    if not os.path.exists(keyfile):
        masterkey = Fernet.generate_key()
        # Store the encrypted key in a file
        with open(keyfile, 'wb') as f:
            f.write(masterkey)
        return masterkey
    else:  # Read and return the key from file
        with open(keyfile, 'rb') as f:
            encrypted_key = f.read()
        return encrypted_key


# Encrypt a message
def encrypt_message(message, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_message = cipher_suite.encrypt(message.encode("utf-8"))
    return encrypted_message


# Decrypt a message
def decrypt_message(encrypted_message, encryption_key):
    cipher_suite = Fernet(encryption_key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


# Returns a decrypted username from the master file
def return_user(encryption_key):
    with open("master.txt", "rb") as masterFile:
        master_user_encrypted = masterFile.readline().strip()
        decrypted_master_user = decrypt_message(master_user_encrypted, encryption_key)
    return decrypted_master_user


# Returns the decrypted password from the master file
def return_pass(encryption_key):
    with open("master.txt", "rb") as masterFile:
        masterFile.readline()  # Skip the first line
        master_pass_encrypted = masterFile.readline().strip()
        decrypted_master_pass = decrypt_message(master_pass_encrypted, encryption_key)
    return decrypted_master_pass

# Encrypts the database
def encrypt_database(encryption_key):
    if os.path.exists("encrypted_key.key"):
        return 0
    else:
        with open("database.txt", "rb") as input_file:
            lines = input_file.readlines()

        with open("database.txt", "wb") as output_file:
            for line in lines:
                encrypted_login = encrypt_message(line.strip().decode("utf-8"), encryption_key.decode("utf-8"))
                output_file.write(encrypted_login + b'\n')
                print(encrypted_login)


# Decrypts the database for and returns it as a list
def decrypt_database(encryption_key):
    decrypted_database = []
    with open("database.txt", "rb") as databaseFile:
        for line in databaseFile:
            login_encrypted = line.strip()
            try:
                decrypted_login = decrypt_message(login_encrypted, encryption_key)
                decrypted_database.append(decrypted_login)
                print("Decrypted login:", decrypted_login)
            except Exception as f:
                print("Error decrypting login:", f)
    return decrypted_database
