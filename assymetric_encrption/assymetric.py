from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#Generate the keys
privkey = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
pubkey = privkey.public_key()

#save the generated keys
#private key
serial_priv = privkey.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open('../hashing folder/private_noshare.pem', 'wb') as f:f.write(serial_priv)

#public key
serial_pub = pubkey.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open('../hashing folder/public_shared.pem', 'wb') as f:f.write(serial_pub)

#reading the encryption keys
#private key
def read_prv(filename="./hashing folder/private_noshare.pem"):
    with open(filename, 'rb') as privkey_file:
        privkey = serialization.load_pem_private_key(
            privkey_file.read(),
            password=None,
            backend=default_backend()
        )
        return privkey

#public key
def read_pub(filename = "./hashing folder/public_shared.pem"):
    with open("../hashing folder/public_shared.pem", 'rb') as pubkey_file:
        pubkey = serialization.load_pem_public_key(
            pubkey_file.read(),
            backend=default_backend()
        )
        return pubkey
#Encryption

def encryption():

    unparsed_data = input("Enter the message you would like to encrypt:\n").encode()
    data = [unparsed_data]

    pubkey = read_pub()

    open('../hashing folder/test.txt', "wb").close()#clear file
    for encode in data:
        encrypted = pubkey.encrypt(
            encode,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open('../hashing folder/test.txt', "ab") as f: f.write(encrypted)


def decryption():
    read_data = []
    privkey = read_prv()
    with open('../hashing folder/test.txt', "rb") as f:
        for encrypted in f:
            read_data.append(
                privkey.decrypt(
                    encrypted,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
            )
    print("decrypted message after decryption", read_data)

encryption()
decryption()

def string_assmetric():
    #create the private and public keys
    (pubkey, privkey)= rsa.newkeys(1024)

    print("private key:\t", privkey)
    print("Public key\t", pubkey)

    #convert this msg to bytes
    msg = b"Top secret message test"

    #encrypt the message with the public key
    crypto = rsa.encrypt(msg, pubkey)
    print("encrypted message:\t", crypto)
    #decryto it with the private key
    decrypt = rsa.decrypt(crypto, privkey)

    #print the orginal message
    print ("Orginal message:\t",decrypt.decode())