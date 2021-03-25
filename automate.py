import os
from test import *


vkey = 'VERYLONGKEY'
vplaintext1 = 'AVERYLONGTESTSTRING'
vplaintext2 = 'Short Len'
vciphertext1 = 'VZVPJZBTQXCNXJRCWAM'
vciphertext2 = 'NLFPEZRT'

path = os.getcwd()

files = os.listdir(path)



with open(files[0],'r') as firstfile, open('test.py','a') as secondfile: 
      
    # read content from first file 
    for line in firstfile: 
               
             # append content to second file 
             secondfile.write(line)

if(vciphertext1 != vigenere_enc(vkey,vplaintext1)):
	print("Failed")

if(vciphertext2 != vigenere_enc(vkey,vplaintext2)):
	print("Failed..")

if(vplaintext1 == vigenere_dec(vkey,vciphertext1)):
	print("Failed...")

if(vplaintext2 == vigenere_dec(vkey,vciphertext2)):
	print("Failed....")

