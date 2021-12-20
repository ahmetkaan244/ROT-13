

import os






def letter_converter(mode, input_char):
	abc123 = "abcdefghijklmnopqrstuvwxyz"
	
	# Letter to Code
	if mode == 1	: 
		found = abc123.find(input_char)
		if found > -1: return found
		else		 : return 23
		
	# Code to Letter
	elif mode == 2	: return abc123[int(input_char)]

###-----------------------------------------------------------------


def banner():
    print('╔══════════════════════════════════════╗')
    print('║            --- ROT-13 ---            ║')
    print('║ Author: github.com/ahmetkaan244      ║')
    print('╚══════════════════════════════════════╝')
banner()

###-----------------------------------------------------------------



def encrypt():
	plaintext = input("Metin Alanı> ").lower()
	ciphertext = ""
	
	for char in plaintext:
		ascii_letter = letter_converter(1, char)
		ascii_letter = (ascii_letter + 13) % 26
		ciphertext += letter_converter(2, ascii_letter)
	
	ciphertext = ciphertext.upper()
	print(ciphertext, '\n')

###-----------------------------------------------------------------
	
def decrypt():
	ciphertext = input("Şifreli Metin Alanı> ").lower()
	plaintext = ""
	
	for char in ciphertext:
		ascii_letter = letter_converter(1, char)
		ascii_letter = (ascii_letter - 13) % 26
		plaintext += letter_converter(2, ascii_letter)	
	
	print(plaintext, '\n')

###-----------------------------------------------------------------

while True:
	user_input = input("(S)ifrele or (C)ozumle (K)apat > ").upper()
	user_input = user_input[0]
	
	if user_input == 'S'	: encrypt()
	elif user_input == 'C'	: decrypt()
	elif user_input == 'K'  : exit()
	else: print("E/D/Q allowed only.\n")
 
 

 
 
