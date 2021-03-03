UID = 116715867                           
Last_Name = 'SALVI'                      
First_Name = 'SAURABH'                


def caesar_str_enc(plaintext, k):                               #k is the encryption key
    ciphertext = ""
    
    for charac in plaintext:

        if(charac == ' '): 
            ciphertext = ciphertext + ' '                       #handling blank space

        else:
            plaintext_ascii = ord(charac)
            plaintext_ascii = plaintext_ascii - 65
            ciphertext_ascii = (plaintext_ascii + k) % 26
            ciphertext = ciphertext + chr(ciphertext_ascii+65)
	
    return ciphertext                         

def caesar_str_dec(ciphertext, k):                              #k is the encryption key
    plaintext = ""
    
    for charac in ciphertext:

        if(charac == ' '): 
            plaintext = plaintext + ' '                         #handling blank space

        else:
            ciphertext_ascii = ord(charac)
            ciphertext_ascii = ciphertext_ascii - 65
            plaintext_ascii = (ciphertext_ascii - k) % 26
            plaintext = plaintext + chr(plaintext_ascii+65)

    return plaintext
	

if __name__ == "__main__":

    print("\nNAME: " + First_Name + ' ' + Last_Name)
    print("UID: " + str(UID))

    print("\n****CAESAR CIPHER ENCRYPTION****")

    input_str = input("\nEnter The String (UPPERCASE ONLY): ")
    k = int(input("Enter The Key (INTEGER ONLY): "))
    #input_str = 'ZZ'
    #k = 2                     

    encstr = caesar_str_enc(input_str,k)
    print("\nENCRYPTED TEXT : " + encstr)
    decstr = caesar_str_dec(encstr, k)
    print("DECRYPTED TEXT : " + decstr)