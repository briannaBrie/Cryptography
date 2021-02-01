#this file signs a file with the owner's private key and
#verifies the signature with the owner's public key
import rsa

#open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data

#open private key file and load in key
privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))

#open the secret message file and return data to a varial
msg = file_open('message.txt')
hash_value= rsa.compute_hash(msg, 'SHA-512')

#sign the message with the owners private key
signature = rsa.sign(msg, privkey, 'SHA-512')

s = open('signature_file.txt', 'wb')
s.write(signature)

print(signature)
print(len(signature))
print(len(hash_value)*8)