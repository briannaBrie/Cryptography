import rsa
#ensuring that the file you have has a dig sign on the sender
#create the pub and private keys
(pubkey, privkey) =rsa.newkeys(2048)

#write teh public key to a file
with open('publickey.key', 'wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))

# write the private  key to a file
with open("privatekey.key", "wb") as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))