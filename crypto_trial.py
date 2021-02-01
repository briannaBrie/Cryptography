import sys
import chilkat

# This example assumes the Chilkat API to have been previously unlocked.
# See Global Unlock Sample for sample code.

rsa = chilkat.CkRsa()

# Generate a 1024-bit key.  Chilkat RSA supports
# key sizes ranging from 512 bits to 4096 bits.
success = rsa.GenerateKey(1024)
if (success != True):
    print(rsa.lastErrorText())
    sys.exit()

# Keys are exported in XML format:
publicKeyXml = rsa.exportPublicKey()
print(publicKeyXml)

privateKeyXml = rsa.exportPrivateKey()
print(privateKeyXml)

# Save the private key in PEM format:
privKey = chilkat.CkPrivateKey()
success = privKey.LoadXml(privateKeyXml)
success = privKey.SaveRsaPemFile("privateKey.pem")

# Save the public key in PEM format:
pubKey = chilkat.CkPublicKey()
success = pubKey.LoadXml(publicKeyXml)
success = pubKey.SaveOpenSslPemFile("publicKey.pem")
