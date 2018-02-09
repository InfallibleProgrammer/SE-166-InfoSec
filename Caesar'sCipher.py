# This .py file was created to bring the concepts taught in class to life.
# Concept: Caesar's Ciphere
# By: Akash Vachhani 
# Date: 2/01/18

ALPHABET = 26 #Number of letters in US English alphabet

def FunctionSelect():
	while 1 == 1:
		mode = input("Enter 'E' for Encrypt and 'D' for Decrypt: ").lower()
		if mode == "e" or mode == "d":
			return mode
		else:
			print("Please enter a valid input! ")
def Algorithm(mode):
	message = input("Please enter the message/password you want encryped: ").lower()
	key = int(input("Enter a key value: "))
	key = key%ALPHABET
	if mode == "d":
		key = -key
	secret = ""
	for char in message:
		if char.islower():
			secret += char
		else:
			newchar = ord(char)+key #ord gets ASCII value. Than adds the key value to it
			if char.islower():
				if newchar > ord('z'):
					newchar -= 26 #Capitals come first in ASCII, so subtract 26 from it to wrap around
				elif newchar > ord('a'):
					newchar += 26 #Wrap around ASCII Value by adding 26 to it. 
			elif char.isupper():
				if newchar > ord('Z'):
					newchar -= 26 #Capitals come first in ASCII, so subtract 26 from it to wrap around
				elif newchar > ord('A'):
					newchar += 26 #Wrap around ASCII Value by adding 26 to it. 
			secret += chr(newchar)
	print("Your translated message is: %s" %(secret))
mode = FunctionSelect()
Algorithm(mode)
