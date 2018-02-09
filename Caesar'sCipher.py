# This .py file was created to bring the concepts taught in class to life.
# Concept: Caesar's Ciphere
# By: Akash Vachhani 
# Date: 2/01/18

import re

ALPHABET = 26 #Number of letters in US English alphabet
a = 97

def FunctionSelect():
	while 1 == 1:
		mode = input("Enter 'E' for Encrypt and 'D' for Decrypt: ").lower()
		if mode == "e" or mode == "d":
			return mode
		else:
			print("Please enter a valid input! ")

def CleanMessage(message):
	message = message.lower()
	message = re.sub("[^a-zA-z\s]","", message)
	return message

def Algorithm(message, mode):
	clean_msg = CleanMessage(message)
	key = int(input("Enter a key value: "))
	key = key % ALPHABET
	if mode == "d":
		key = -key
	secret = ""
	for char in clean_msg:
		if char == " ":
			secret += " "
		else:
			newchar = chr(((((ord(char)-a)+key)%ALPHABET)) + a) #shift relationship
			#get the ascii value, subtract a which is 97, than mod with ALPHABET than add 97
			#to get new ASCII Value. Take chr of that value to get the letter.
			secret += newchar
	return secret
	
mode = FunctionSelect()

message = input("Please enter the message/password you want encryped: ")

secret = Algorithm(message, mode)

print("Your translated message is: %s" %(secret))
