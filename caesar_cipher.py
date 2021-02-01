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

def caesar_encrypt():
    shift = 3 # defining the shift count
    text = "HELLO WORLD"
    encryption = ""
    for c in text:
        # check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            # perform the shift
            new_index = (c_index + shift) % 26
            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to encrypted string
            encryption = encryption + new_character

        else:

            # since character is not uppercase, leave it as it is
            encryption += c
        
    print("Plain text:",text)

    print("Encrypted text:",encryption)


def caesar_decrypt():
    shift = 3 # defining the shift count
    encrypted_text = "KHOOR ZRUOG"
    plain_text = ""

    for c in encrypted_text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the negative shift
            new_index = (c_index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to plain string
            plain_text = plain_text + new_character

        else:

            # since character is not uppercase, leave it as it is
            plain_text += c

    print("Encrypted text:",encrypted_text)

    print("Decrypted text:",plain_text)

caesar_decrypt_caps()
#caesar_encrypt_caps()
