# This .py file was created to bring the concepts taught in class to life.
# Concept: Caesar's Ciphere
# By: Akash Vachhani 
# Date: 2/01/18

import re

def CleanMessage(message):
    message = message.lower()
    message = re.sub("[^a-z\s]", "", message)
    return message

def CaesarCipher(message, key, encrypt):
    ALPHABET = 26 #Number of letters in US English alphabet
    a = 97

    clean_msg = CleanMessage(message)
    key = key % ALPHABET
    
    if encrypt:
        key = -key
    
    secret = ""
    for char in clean_msg:
        if char == " ":
            secret += char
        else:
            newchar = chr(((((ord(char) - a) + key) % ALPHABET)) + a)
            #shift relationship
            #get the ascii value, subtract a which is 97, than mod with ALPHABET than add 97
            #to get new ASCII Value. Take chr of that value to get the letter.
            secret += newchar
    return secret



encrypt = bool()
while True:
    mode = input("Enter 'E' for Encrypt or 'D' for Decrypt: ").lower()
    if mode == 'e':
        encrypt = True
    elif mode == 'd':
        encrypt = False
    else:
        continue
    break

key = int(input("Enter a key value: "))
message = input("Please enter the message/password you want encryped: ")
secret = CaesarCipher(message, key, encrypt)

print("Your translated message is: {}".format(secret))