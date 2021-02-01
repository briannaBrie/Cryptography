def user_choice():
    user = input("Choose the encryption /Decrption scheme you would like to use:\n "+
    "1. Reverse a string\n 2. Reverse string two by two letters\n 3. reverse string three by three letters\n"+
    " 4. Caesar cypher like encryption\n 5. Caesar cypher like decryption\n ")
    
    if(user !=""):
        choice = int(user)
        if(choice ==1):
            reverseString()
        elif (choice == 2):
            rev2()
        elif (choice == 3):
            rev3()
        elif(choice == 4):
            caesar_encrypt_caps()
        elif(choice == 5):
            caesar_decrypt_caps()
        elif(choice >=6 or choice <= 0):
            print("Invalid choice, please try again")

def caesar_encrypt_caps():
    #encryption for caps using caesar cipher
    msg = input("Enter the message to encrypt:\t")
    shift = input("Enter the encryption key:\t")

    if shift !="":
        shift = int(shift)

        shift_encrypt_method(shift, msg)

    else:
        shift = 3
        shift_encrypt_method(shift, msg)

def caesar_decrypt_caps():
    #encryption for caps using caesar cipher
    msg = input("Enter the message to decrypt:\t")
    shift = input("Enter the encryption key:\t")

    if shift !="":
        shift = int(shift)

        shift_decrypt_method(shift, msg)

    else:
        shift = 3
        shift_decrypt_method(shift, msg)

def shift_encrypt_method(shift,msg):
    encrypted_msg = ""
    for c in msg:
        #check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_index = ord(c) - ord("A")
            #perform the shift
            new_index = (c_index + shift) % 26
            #convert character
            new_unicode = new_index + ord("A")
            new_char = chr(new_unicode)

            #append to encrypted string
            encrypted_msg = encrypted_msg + new_char
        else:
            #leave as it is
            encrypted_msg += c

    print("Orginial message:\t", msg)
    print("Encrypted message:\t", encrypted_msg)

def shift_decrypt_method(shift,msg):
    decrypted_msg = ""

    for c in msg:

        # check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_index = ord(c) - ord("A")
            # perform the negative shift
            new_index = (c_index - shift) % 26
            # convert to new character
            new_unicode = new_index + ord("A")
            new_char = chr(new_unicode)
            # append to plain string
            decrypted_msg = decrypted_msg + new_char
        else:
            #leave it as it is
            decrypted_msg += c

    print("Encrypted message:\t", msg)
    print("Decrypted message:\t", decrypted_msg)

def rev3():
    a = input("Enter your string:\n")
    rev_string= ""
    rev_string= "".join([a[x:x+3] for x in range(0,len(a),3)][::-1])

    print("Original String:\t", a)
    print("Reversed by 3 str: \t", rev_string )

def rev2():
    org_string= input("Enter your string:\n")
    rev_string= ""
    rev_string ="".join(reversed([org_string[i:i+2] for i in range(0, len(org_string), 2)])) 

    print("Original String:\t", org_string)
    print("Reversed by 2 str:\t", rev_string)

def OddEven():
    str1 = input("Enter your String \n")
    str2 = ''
    str3 = ''
    for i in range(1, len(str1)+1):
        if(i % 2 ==0):
            str2 = str2 + str1[i-1]
        elif(i % 2 !=0):
            str3 = str3 + str1[i-1]
    
    print ("Original Text:\t", str1)
    print("Even String:\t", str2)
    print("Odd String:\t", str3)

def reverseString():
    rvs = input("Enter your string: ")
    print(rvs[::-1])

user_choice()