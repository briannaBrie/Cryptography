from cryptography.fernet import Fernet
def generate_key():
    key = Fernet.generate_key()
    #write the key to a file
    fkey = open("file_key.txt", 'wb')
    fkey.write(key)

#read the key from the file
fkey = open("file_key.txt", 'wb')
key = fkey.read()
cipher = Fernet(key)
print(key)

encrypted_text = cipher.encrypt(b'this is my test message')

print(encrypted_text)

org_text = cipher.decrypt(encrypted_text)

print(org_text.decode())
