from cryptography.fernet import Fernet

def write_key():
    #Generate a key and save it to a file
    key = Fernet.generate_key()
    with open("../hashing folder/key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    #loads the key to the correct directory
    return open("../hashing folder/key.key", "rb").read()

def encrypt_decrypt():
    # generate and write a new key
    write_key()
    # load the key
    key = load_key()
    msg = input("Enter Message to decode:\n").encode()

    # initialize fernet class
    f = Fernet(key)
    # encrypt the message
    encrypted = f.encrypt(msg)

    print("Encrypted message", encrypted)
    # encrypt the message
    decrypted_encrypted = f.decrypt(encrypted).decode()

    print("Decrypted message", decrypted_encrypted)

encrypt_decrypt()


