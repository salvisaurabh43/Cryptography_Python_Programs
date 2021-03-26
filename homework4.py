from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad


UID = 116715867                           
Last_Name = 'SALVI'                      
First_Name = 'SAURABH'     

def encrypt_file(in_file,des_key,aes_key,des_cipher_file,aes_cipher_file):

	des_cipher_list = []
	aes_cipher_list = []

	finp = open(in_file,"rb")
	des_fout = open(des_cipher_file,"wb")
	aes_fout = open(aes_cipher_file,"wb")

	filebytes = finp.read()


	
	#DES ENCRYPTION

	filebytes_plain_des_list = [filebytes[i:i+8] for i in range(0, len(filebytes), 8)]			#dividing into chunks of 8

	list_len = len(filebytes_plain_des_list)			

	filebytes_plain_des_list[list_len - 1] = pad(filebytes_plain_des_list[list_len - 1], 8)		#padding the last chunk
	#print(filebytes_plain_des_list)

	des_cipher = DES.new(des_key, DES.MODE_ECB)

	for chunks in filebytes_plain_des_list:
		des_cipher_list.append(des_cipher.encrypt(chunks))

	des_ciphertext = b''.join(des_cipher_list)


	des_fout.write(des_ciphertext)

	print(bytes(des_ciphertext))

	#AES ENCRYPTION

	filebytes_plain_aes_list = [filebytes[i:i+16] for i in range(0, len(filebytes), 16)]			#dividing into chunks of 16

	list_len = len(filebytes_plain_aes_list)			

	filebytes_plain_aes_list[list_len - 1] = pad(filebytes_plain_aes_list[list_len - 1], 16)		#padding the last chunk
	
	

	aes_cipher = AES.new(aes_key, AES.MODE_ECB)

	for chunks in filebytes_plain_aes_list:
		aes_cipher_list.append(aes_cipher.encrypt(chunks))

	aes_ciphertext = b''.join(aes_cipher_list)

	aes_fout.write(aes_ciphertext)

	print(bytes(aes_ciphertext))

	finp.close()
	des_fout.close()
	aes_fout.close()

def decrypt_file(des_cipher_file,aes_cipher_file,des_key,aes_key,des_plain_file,aes_plain_file):

	des_plain_list = []
	aes_plain_list = []

	des_finp = open(des_cipher_file,"rb")
	des_fout = open(des_plain_file,"wb")
	des_filebytes = des_finp.read()


	


	#DES DECRYPTION

	filebytes_cipher_des_list = [des_filebytes[i:i+8] for i in range(0, len(des_filebytes), 8)]			#dividing into chunks of 8

	list_len = len(filebytes_cipher_des_list)			

	des_cipher = DES.new(des_key, DES.MODE_ECB)


	for chunks in filebytes_cipher_des_list:
		des_plain_list.append(des_cipher.decrypt(chunks))

	des_plaintext_padded = b''.join(des_plain_list)

	des_plaintext = unpad(des_plaintext_padded, 8)



	des_fout.write(des_plaintext)

	#AES DECRYPTION

	aes_finp = open(aes_cipher_file,"rb")
	aes_fout = open(aes_plain_file,"wb")
	aes_filebytes = aes_finp.read()


	filebytes_cipher_aes_list = [aes_filebytes[i:i+16] for i in range(0, len(aes_filebytes), 16)]			#dividing into chunks of 16

	list_len = len(filebytes_cipher_aes_list)			


	aes_cipher = AES.new(aes_key, AES.MODE_ECB)

	for chunks in filebytes_cipher_aes_list:
		aes_plain_list.append(aes_cipher.decrypt(chunks))

	aes_plaintext_padded = b''.join(aes_plain_list)

	aes_plaintext = unpad(aes_plaintext_padded, 16)


	aes_fout.write(aes_plaintext)

	print(bytes(aes_plaintext))

	des_fout.close()
	aes_fout.close()


def aes_input_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte long bytes values each
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption on the new input with one inverted bit at position b
        newcipher = aes_enc(newinput, key)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list


def aes_input_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte long bytes values each
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption on the new input with one inverted bit at position b
        newcipher = aes_enc(newinput, key)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list


# We also perform similar experiment by keeping the inputblock fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        newkey = invertbit(key, b)
        
        # perform encryption with the new key with one inverted bit at position b
        newcipher = aes_enc(inputblock, newkey)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list


def aes_enc(inputblock, key):

	aes_input_padded = pad(inputblock, 16)
	aes_cipher = AES.new(key, AES.MODE_ECB)
	aes_ciphertext = aes_cipher.encrypt(aes_input_padded)

	return aes_ciphertext




if __name__ == "__main__":

	encrypt_file('input.txt',b'8bytekey',b'veryverylongkey!','des_cipher.txt','aes_cipher.txt')
	decrypt_file('des_cipher.txt','aes_cipher.txt',b'8bytekey',b'veryverylongkey!','des_plain.txt','aes_plain.txt')





	
