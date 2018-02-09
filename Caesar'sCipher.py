# This .py file was created to bring the concepts taught in class to life.
# Concept: Caesar's Ciphere
# By: Akash Vachhani 
# Date: 2/01/18

import re

ALPHABET = 26 #Number of letters in US English alphabet

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
	for char in message:
		# Write code here for shifting
	return secret
	
mode = FunctionSelect()

message = input("Please enter the message/password you want encryped: ")

secret = Algorithm(message, mode)

print("Your translated message is: %s" %(secret))
