import string
letter = list(string.ascii_lowercase)
# upper = list(string.ascii_uppercase)
# print(letter)
def enc (msg,key):
    encrypted_msg = ""
    for char in msg:
        if char in letter:
            position = letter.index(char) 
            enc_msg = (position+key)%26
            encrypted_msg += letter[enc_msg]
        else:
            encrypted_msg += char
    print(f"Encrypted message : {encrypted_msg}")

def dec(msg,key):
    decrypted_msg = ""
    for char in msg:
        if char in letter:
            position = letter.index(char)
            dec_msg = (position-key)%26
            decrypted_msg += letter[dec_msg]
        else:
            decrypted_msg += char
    print(f"Decrypted message : {decrypted_msg}")
    
flag = False
while not flag:
    user = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    message = input("Type your message:\n").lower()
    num = int(input("Type the shift number:\n"))
    if user == "encrypt":
        enc (msg=message, key= num)
    elif user == "decrypt":
        dec (msg=message, key= num)
    check = input("Type 'yes' to continue & 'no' to exit. :")
    if check == "yes":
        flag = False
    elif check == "no":
        flag = True



