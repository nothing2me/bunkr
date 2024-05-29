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
    else: # Read and return the key from file
        with open(keyfile, 'rb') as f:
            encrypted_key = f.read()
        return encrypted_key

# Encrypt a message
def encrypt_message(message, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message, encryption_key):
    cipher_suite = Fernet(encryption_key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Returns a decrypted username from the master file
def return_user(encryption_key):
    with open("master.txt", "rb") as masterFile:
        masterUser_encrypted = masterFile.readline().strip()
        decrypted_masterUser = decrypt_message(masterUser_encrypted, encryption_key)
    return decrypted_masterUser

# Returns the decrypted password from the master file
def return_pass(encryption_key):
    with open("master.txt", "rb") as masterFile:
        masterFile.readline()  # Skip the first line
        masterPass_encrypted = masterFile.readline().strip()
        decrypted_masterPass = decrypt_message(masterPass_encrypted, encryption_key)
    return decrypted_masterPass
