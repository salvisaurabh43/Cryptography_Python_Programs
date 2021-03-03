import numpy as np
from pprint import pprint



UID = 116715867                           
Last_Name = 'SALVI'                      
First_Name = 'SAURABH'              

def vigenere_enc(key,plaintext):

	plaintext_len = len(plaintext)
	vigenere_key = ''
	ciphertext_ascii = ''
	ciphertext = ''
	j=0

	for i in range(0,plaintext_len):
		if j == len(key):
			j = 0
			vigenere_key = vigenere_key + key[j]
		else:
			vigenere_key = vigenere_key + key[j]
		j = j + 1;

	for i in range(0,plaintext_len):
		plaintext_ascii = ord(plaintext[i])
		vigenere_key_ascii = ord(vigenere_key[i])
		ciphertext_ascii = ((plaintext_ascii - 65) + (vigenere_key_ascii - 65)) % 26
		ciphertext = ciphertext + chr(ciphertext_ascii+65)

	return ciphertext

def vigenere_dec(key,ciphertext):
	
	ciphertext_len = len(ciphertext)
	vigenere_key = ''
	plaintext_ascii = ''
	plaintext = ''
	j=0

	for i in range(0,ciphertext_len):
		if j == len(key):
			j = 0
			vigenere_key = vigenere_key + key[j]
		else:
			vigenere_key = vigenere_key + key[j]
		j = j + 1;

	for i in range(0,ciphertext_len):
		ciphertext_ascii = ord(ciphertext[i])
		vigenere_key_ascii = ord(vigenere_key[i])
		plaintext_ascii = ((ciphertext_ascii - 65) - (vigenere_key_ascii - 65)) % 26
		plaintext = plaintext + chr(plaintext_ascii+65)

	return plaintext

def hill_dec(M, cipher_string):
	
	cipher_string_array_ascii = []
	cipher_sub_string_array_ascii = []
	sub_string_array_ascii = []
	string_array_ascii = []
	string_array = []

	Minv = np.linalg.inv(M)
	Mdet = np.linalg.det(M)
	

	np.matrix.round(np.matmul(M, Minv))			# M * Minv = Integer Matrix

	Madj = Mdet*Minv
	Madj26 = Madj%26

	Mdet26 = Mdet%26

	Mod26invTable = {}
	for m in range(26):
		for minv in range(26):
			if(m*minv)%26==1:
				Mod26invTable[m] = minv

	if Mdet26 in Mod26invTable:
		Mdet26inv = Mod26invTable[Mdet26]
	else:
		Mdet26inv = -1

	Minv26 = (Mdet26inv*Madj26)%26				# Matrix M inverse
	

	for i in range(0,len(cipher_string)):
		cipher_string_array_ascii.append(ord(cipher_string[i]) - 65)

	strlen_by_3 = int(len(cipher_string)/3)

	for i in range(0,strlen_by_3):
		cipher_sub_string_array_ascii.append(cipher_string_array_ascii[3*i:(3*i+3)])

	cipher_sub_string_array_ascii = np.array(cipher_sub_string_array_ascii)

	for i in range(0,len(cipher_sub_string_array_ascii)):
		sub_string_array_ascii.append(np.matrix.round(np.matmul(cipher_sub_string_array_ascii[i],Minv26))%26)

	for i in range(0,len(sub_string_array_ascii)):
		for j in range(0,3):
			string_array_ascii.append(int(sub_string_array_ascii[i][j]))	

	for i in range(0,len(string_array_ascii)):
		string_array.append(chr(string_array_ascii[i] + 65))

	plain_string = ''
	plain_string = plain_string.join(string_array)

	test = np.matrix.round(np.matmul(M,Minv26))%26


	return plain_string 


def hill_enc(M, plaintext):

	input_str = plaintext

    
	string_array_ascii = []

	sub_string_array_ascii = []

	cipher_sub_string_array_ascii = []

	cipher_string_array_ascii = []

	cipher_string_array = []

	for i in range(0,len(input_str)):
		string_array_ascii.append(ord(input_str[i]) - 65)

	strlen_by_3 = int(len(input_str)/3)

	for i in range(0,strlen_by_3):
		sub_string_array_ascii.append(string_array_ascii[3*i:(3*i+3)])

	sub_string_array_ascii = np.array(sub_string_array_ascii)
	
	for i in range(0,len(sub_string_array_ascii)):
		cipher_sub_string_array_ascii.append(np.matrix.round(np.matmul(sub_string_array_ascii[i],M))%26)


	for i in range(0,len(cipher_sub_string_array_ascii)):
		for j in range(0,3):
			cipher_string_array_ascii.append(cipher_sub_string_array_ascii[i][j])

	
	for i in range(0,len(cipher_string_array_ascii)):
		cipher_string_array.append(chr(cipher_string_array_ascii[i] + 65))


	cipher_string = ''
	cipher_string = cipher_string.join(cipher_string_array)

	return cipher_string
	
def modify_input_for_vigenere(input_str):
	
	input_str_upper = input_str.upper()
	input_str_nospace = input_str_upper.replace(' ','')

	input_str_len = len(input_str_nospace)

	return input_str_nospace

def modify_input_for_hill(input_str):
	
	input_str_upper = input_str.upper()
	input_str_nospace = input_str_upper.replace(' ','')

	input_str_len = len(input_str_nospace)

	if(input_str_len % 3 == 1):
		input_str_nospace = input_str_nospace + "XX"
	elif(input_str_len % 3 == 2): 
		input_str_nospace = input_str_nospace + "X"

	return input_str_nospace


if __name__ == "__main__":

    print("\nNAME: " + First_Name + ' ' + Last_Name)
    print("UID: " + str(UID))

    
    print("\n****VIGENERE CIPHER ENCRYPTION****")

    input_str = input("\nEnter The String : ")

    input_str = modify_input_for_vigenere(input_str)

    key = input("Enter The Key String : ")

    encstr = vigenere_enc(key,input_str)
    print("\nENCRYPTED TEXT : " + encstr)

    decstr = vigenere_dec(key,encstr)
    print("DECRYPTED TEXT : " + decstr)

    

    print("\n****HILL CIPHER ENCRYPTION****")

    input_str = input("\nEnter The String : ")
    #k = int(input("Enter The Key (INTEGER ONLY): "))

    input_str = modify_input_for_hill(input_str)

    M = np.array([[17,17,5],[21,18,21],[2,2,19]])
           
    encstr = hill_enc(M,input_str)
    print("\nENCRYPTED TEXT : " + encstr)
    
    decstr = hill_dec(M,encstr)
    print("DECRYPTED TEXT : " + decstr)



