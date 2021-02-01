import hashlib
import glob
import os
import os.path as osp


def menu():
    obj = input("Choose the hashing algorithm:\n 1 - hash a string\n 2 - hash a file\n 3 - hash a content of the folder\n")
    menu_ = input(" 1. sha1\n 2. sha224\n 3. sha384\n 4. blake2s\n 5. shake_128\n 6. md5\n")

    if(obj !="" and menu_ !=""):
        obje = int(obj)
        menus = int(menu_)
        #hashing a string
        if(obje == 1):
            if(menus == 1):
                hash_string_sha1()
            elif(menus == 2):
                hash_string_sha224()
            elif(menus == 3):
                hash_string_sha384()
            elif(menus == 4):
                hash_string_blake2s()
            elif(menus == 5):
                hash_string_shake_128()
            elif(menus == 6):
                hash_string_md5()
            elif(menus<=0 or menus>=7):
                print("Invalid menu input try again")

        #hashing files        
        elif(obje == 2):
            if(menus == 1):
                hash_file_sha1()
            elif(menus == 2):
                hash_file_sha224()
            elif(menus == 3):
                hash_file_sha384()
            elif(menus == 4):
                hash_file_blake2s()
            elif(menus == 5):
                hash_file_shake_128()
            elif(menus == 6):
                hash_file_md5()
            elif(menus<=0 or menus>=7):
                print("Invalid menu input try again")
        
        #hashing folders
        elif(obje == 3):
            cur = input("Choose: \n 1. Recursive\n 2. Cursive\n")
            if(cur !=""):
                curs = int(cur)
                #recursive folder hash
                if(curs == 1):
                    if(menus ==1):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_sha1(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name))

                    elif(menus ==2):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_sha224(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name))
                    
                    elif(menus ==3):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_sha384(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name))                    
                    
                    elif(menus ==4):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_blake2s(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name))

                    elif(menus ==5):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_shake128(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name))

                    elif(menus ==6):
                        ROOT = './hashing folder'
                        for root, dirs, files in os.walk(ROOT):
                            for fpath in [osp.join(root, f) for f in files]:
                                sha = filehash_md5(fpath)
                                name = osp.relpath(fpath, ROOT)
                                write('%s,%s' % (sha, name)) 

                elif(curs == 2):
                    #non-recusive hashing
                    if(menus == 1):
                        hash_folder_sha1()
                    elif(menus == 2):
                       hash_folder_sha224()
                    elif(menus == 3):
                        hash_folder_sha384()
                    elif(menus == 4):
                        hash_folder_blake2s()
                    elif(menus == 5):
                        hash_folder_shake128()
                    elif(menus == 6):
                        hash_folder_md5()
                elif(curs<=0 or curs >=2):
                    print("Invalid folder hashing input. Try again")
        elif(obje <=0 or obje >=4):
            print("Invalid hashing input. Try again")


def hash_folder_sha224():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.sha224(data).hexdigest(), filename)

def hash_folder_sha384():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.sha384(data).hexdigest(), filename)

def hash_folder_blake2s():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.blake2s(data).hexdigest(), filename)

def hash_folder_shake128():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.shake_128(data).hexdigest(), filename)

def hash_folder_md5():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.md5(data).hexdigest(), filename)

def hash_folder_sha1():
    #filenames = glob.glob("C:/Users/bridg/OneDrive/Documents/School Projects/Cryptography/hashing folder/*.txt")
    files = glob.glob("./hashing folder/*.txt")
    #filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")
    for filename in files:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            print(hashlib.sha1(data).hexdigest(), filename)


def filehash_md5(filepath):
    blocksize = 64*1024
    sha = hashlib.md5()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def filehash_shake128(filepath):
    blocksize = 64*1024
    sha = hashlib.shake_256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def filehash_blake2s(filepath):
    blocksize = 64*1024
    sha = hashlib.blake2s()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def filehash_sha384(filepath):
    blocksize = 64*1024
    sha = hashlib.sha384()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def filehash_sha224(filepath):
    blocksize = 64*1024
    sha = hashlib.sha224()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def filehash_sha1(filepath):
    blocksize = 64*1024
    sha = hashlib.sha1()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

def hash_string_sha1():
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.sha1(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)

def hash_string_md5():
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.md5(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)

def hash_string_shake_128():
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.shake_128(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)

def hash_string_blake2s(): 
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.blake2s(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)

def hash_string_sha384():
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.sha384(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)

def hash_string_sha224():
    res = input("Enter hashing message:\n")

    # convert string to byte  
    res_byte = bytes(res, 'utf-8') 
    hash_object = hashlib.sha224(res_byte)
    hex_dig = hash_object.hexdigest()

    print("Hashed string:\t",hex_dig)    

def hash_file_sha1():
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def hash_file_blake2s():
    BLOCKSIZE = 65536
    hasher = hashlib.blake2s()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def hash_file_sha384():
    BLOCKSIZE = 65536
    hasher = hashlib.sha384()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def hash_file_sha224():
    BLOCKSIZE = 65536
    hasher = hashlib.sha224()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def hash_file_shake_128():
    BLOCKSIZE = 65536
    hasher = hashlib.shake_128()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def hash_file_md5():
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    filename = './hashing folder/hash.txt'
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("Hashed file:\t", filename)

def recursive_folder_hash():
    ROOT = './hashing folder'
    for root, dirs, files in os.walk(ROOT):
        for fpath in [osp.join(root, f) for f in files]:
            size = osp.getsize(fpath)
            sha = filehash_sha1(fpath)
            name = osp.relpath(fpath, ROOT)
            write('%s,%s,%s' % (sha, name, size))

def write(text):
    """ helper for writing output, as a single point for replacement """
    print(text)



menu()
