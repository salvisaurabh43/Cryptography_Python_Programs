from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad


def wrong_encrypt_file(in_file,des_key,aes_key,des_cipher_file,aes_cipher_file):

	finp = open(in_file,"rb")
	des_fout = open(des_cipher_file,"wb")
	aes_fout = open(aes_cipher_file,"wb")

	filebytes = finp.read()

			#DES ENCRYPTION

	des_filebytes = pad(filebytes, 8)
	des_cipher = DES.new(des_key, DES.MODE_ECB)
	des_ciphertext = des_cipher.encrypt(des_filebytes)
	#print(des_ciphertext.hex())
	des_fout.write(des_ciphertext)

			#AES ENCRYPTION

	aes_filebytes = pad(filebytes, 16)
	aes_cipher = AES.new(aes_key, AES.MODE_ECB)
	aes_ciphertext = aes_cipher.encrypt(aes_filebytes)
	#print(aes_ciphertext.hex())
	aes_fout.write(aes_ciphertext)

	return 0

def wrong_decrypt_file(des_cipher_file,aes_cipher_file,des_key,aes_key,des_plain_file,aes_plain_file):

			#AES DECRYPTION

	des_finp = open(des_cipher_file,"rb")
	des_fout = open(des_plain_file,"wb")
	des_filebytes = des_finp.read()

	des_cipher = DES.new(des_key, DES.MODE_ECB)
	des_plaintext_padded = des_cipher.decrypt(des_filebytes)
	des_plaintext = unpad(des_plaintext_padded, 8)

	des_fout.write(des_plaintext)


			#AES DECRYPTION

	aes_finp = open(aes_cipher_file,"rb")
	aes_fout = open(aes_plain_file,"wb")
	aes_filebytes = aes_finp.read()

	aes_cipher = AES.new(aes_key, AES.MODE_ECB)
	aes_plaintext_padded = aes_cipher.decrypt(aes_filebytes)
	aes_plaintext = unpad(aes_plaintext_padded, 16)

	aes_fout.write(aes_plaintext)

	return 0


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

	#AES ENCRYPTION

	filebytes_plain_aes_list = [filebytes[i:i+16] for i in range(0, len(filebytes), 16)]			#dividing into chunks of 16

	list_len = len(filebytes_plain_aes_list)			

	filebytes_plain_aes_list[list_len - 1] = pad(filebytes_plain_aes_list[list_len - 1], 16)		#padding the last chunk
	
	

	aes_cipher = AES.new(aes_key, AES.MODE_ECB)

	for chunks in filebytes_plain_aes_list:
		aes_cipher_list.append(aes_cipher.encrypt(chunks))

	aes_ciphertext = b''.join(aes_cipher_list)

	aes_fout.write(aes_ciphertext)


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



if __name__ == "__main__":

	#wrong_encrypt_file('test.py',b'8bytekey',b'veryverylongkey!','des_cipher.txt','aes_cipher.txt')
	encrypt_file('test.py',b'8bytekey',b'veryverylongkey!','des_cipher.txt','aes_cipher.txt')
	wrong_decrypt_file('des_cipher.txt','aes_cipher.txt',b'8bytekey',b'veryverylongkey!','des_plain.txt','aes_plain.txt')
	decrypt_file('des_cipher.txt','aes_cipher.txt',b'8bytekey',b'veryverylongkey!','des_plain.txt','aes_plain.txt')
	


# in a loop:
# break the filebytes into 16 bytes chunks using indexing filebytes[0:15], filebytes[16:31], etc.
# apply encryption to each 16 bytes chunk
# ciphertext = ....
# fout.write(ciphertext)
# after the end of the loop close your output file as well
# fout.close()