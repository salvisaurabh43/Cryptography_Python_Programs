import hmac
import hashlib
import random
import lib

UID = 116715867                           
Last_Name = 'SALVI'                      
First_Name = 'SAURABH'

def feistel_block(LE_inp, RE_inp, k):

	LE_out = RE_inp
	F_result = F(RE_inp,k)
	RE_out = xor(LE_inp,F_result)
	return LE_out, RE_out

def xor(byteseq1, byteseq2):
	l1 = [b for b in byteseq1]
	l2 = [b for b in byteseq2]
	l1attachl2 = zip(l1,l2)

	l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in l1attachl2]
	#print(l1xorl2)

	result = b''.join(l1xorl2)
	#print(result)

	return result


def gen_keylist(keylenbytes, numkeys, seed):
	# We need to generate numkeys keys each being keylen bytes long
	keylist = []
	random.seed(seed)
   
	keylist = []
	for i in range(numkeys):
		bytelist = b''.join([bytes([random.randint(0,255)]) for x in range(keylenbytes)])
		keylist.append(bytelist)

	return keylist

def feistel_enc(inputbyteseq, num_rounds, seed):
	

	if(len(inputbyteseq) < 16):
		inputbyteseq = set_padding(inputbyteseq)
	elif(len(inputbyteseq) > 16):
		exit("Input is more than 16 bytes!")

	# first generate the required keys
	keylist = gen_keylist(8, num_rounds, seed)


	seq_length = len(inputbyteseq)

	LE_inp = inputbyteseq[0:8]
	RE_inp = inputbyteseq[8:]
	for i in range(0,num_rounds):
		LE_inp, RE_inp = feistel_block(LE_inp, RE_inp, keylist[i])

	cipherblock = RE_inp + LE_inp

	return cipherblock

def set_padding(inputbyteseq):
	
	seq_length = len(inputbyteseq)

	for i in range(seq_length, 16):
		inputbyteseq = inputbyteseq + b'\x20'

	return inputbyteseq

def feistel_dec(inputbyteseq, num_rounds, seed):

	# Make sure you use the keys in reverse order during decryption
	keylist = gen_keylist(8, num_rounds, seed)

	keylist.reverse()

	# apply the num_rounds times of the block funciton

	seq_length = len(inputbyteseq)

	LE_inp = inputbyteseq[0:8]
	RE_inp = inputbyteseq[8:]


	for i in range(0,num_rounds):
		LE_inp, RE_inp = feistel_block(LE_inp, RE_inp, keylist[i])

	plaintextblock = RE_inp + LE_inp

	return plaintextblock



def F(byteseq, k):

	# we use the hmac hash (don't worry about the meaning for now)
	h = hmac.new(k, byteseq, hashlib.sha1)
	# return the first 8 bytes of the hash value
	return h.digest()[:8]



if __name__ == "__main__":

    print("\nNAME: " + First_Name + ' ' + Last_Name)
    print("UID: " + str(UID))

    print("\n****FEISTEL CIPHER ENCRYPTION****")

    ciphertextblock = feistel_enc(b'isthis16bytes?',16,50)

    plaintextblock = feistel_dec(ciphertextblock,16,50)

    print("\nENCRYPTED TEXT : " , ciphertextblock)

    print("DECRYPTED TEXT : " , plaintextblock)

