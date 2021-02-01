import rsa

#open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data

#open public key file and load in key
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))

msg = file_open('message.txt')
signature = file_open('signature_file.txt')

#verify the signature to show if successful or failed
try:
    rsa.verify(msg, signature,pubkey)
    print("Signature successfully verified")

except:
    print("Warning!!! Signature could not be verified")

