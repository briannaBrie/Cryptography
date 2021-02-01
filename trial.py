import hashlib
import glob
import os
import os.path as osp


def hash_string():
    res = input("Enter hashing message")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.sha1(res_byte)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)

def hash_file_sha256():
    file = ".\hash.txt" # Location of the file (can be set a different way)
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash

def hash_file():
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open('hash.txt', 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print(hasher.hexdigest())

def hash_folder():

    filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")

    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(filename, hashlib.md5(data).hexdigest())


# --- helpers ---

def write(text):
    """ helper for writing output, as a single point for replacement """
    print(text)

def filehash(filepath):
    blocksize = 64*1024
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

# --- /helpers ---


#write("""\
#%%%% HASHDEEP-1.0
#%%%% size,sha256,filename
##
## $ hashdeep.py
##""")

ROOT = './hashing folder'
for root, dirs, files in os.walk(ROOT):
    for fpath in [osp.join(root, f) for f in files]:
        size = osp.getsize(fpath)
        sha = filehash(fpath)
        name = osp.relpath(fpath, ROOT)
        write('%s,%s,%s' % (size, sha, name))
