import importlib

def test_script(module_name):
    list_msg = []
    try:
        c = importlib.import_module(module_name[:-3])
        try:
            UID = c.UID
            if UID is None:
                list_msg.append('UID value is not set')
        except Exception as e:
            list_msg.append('Global variable \'UID\' doesn\'t exist')
        
        try:
            Last_Name = c.Last_Name
            if Last_Name is None:
                list_msg.append('Last_Name value is not set')
        except Exception as e:
            list_msg.append('Global variable \'Last_Name\' doesn\'t exist')
        
        try:
            First_Name = c.First_Name
            if First_Name is None:
                list_msg.append('First_Name value is not set')
        except Exception as e:
            list_msg.append('Global variable \'First_Name\' doesn\'t exist')
        
        try:
            result = c.aes_input_av_test(b'isthis16bytes?',b'veryverylongkey!',[5,29,38])
            if result is None:
                list_msg.append('The function "aes_input_av_test" does not return any value')
            elif not isinstance(result,list):
                list_msg.append('The function "aes_input_av_test" does not return a list')
        except Exception as e:
            print('inp' + e)
            list_msg.append('The function "aes_input_av_test" either doesn\'t exist or does not accept the correct number of arguments or has invalid argument type or returned an error')
        
        try:
            result = c.aes_key_av_test(b'isthis16bytes?',b'veryverylongkey!',[5, 29, 38])
            if result is None:
                list_msg.append('The function "aes_key_av_test" does not return any value')
            elif not isinstance(result,list):
                list_msg.append('The function "aes_key_av_test" does not return a list')
        except Exception as e:
            print(e)
            list_msg.append('The function "aes_key_av_test" either doesn\'t exist or does not accept the correct number of arguments or has invalid argument type or returned an error')

        try:
            result = c.encrypt_file('input.txt',b'8bytekey',b'veryverylongkey!','des_output_e.txt','aes_output_e.txt')
            if result == 0:
                f = open('des_output_e.txt','rb')
                des_val = f.read()
                f.close()
                if len(des_val) == 0:
                    list_msg.append('The function "encrypt_file" created an empty file for DES encrypted output')
                f = open('aes_output_e.txt','rb')
                aes_val = f.read()
                f.close()
                if len(aes_val) == 0:
                    list_msg.append('The function "encrypt_file" created an empty file for AES encrypted output')
            else:
                list_msg.append('The function "encrypt_file" does not return 0')
        except Exception as e:
            print(e)
            list_msg.append('The function "encrypt_file" either doesn\'t exist or does not accept the correct number of arguments or has invalid argument type or returned an error')
        
        try:
            result = c.decrypt_file('des_input.txt','aes_input.txt',b'8bytekey',b'veryverylongkey!','des_output_d.txt','aes_output_d.txt')
            if result == 0:
                f = open('des_output_e.txt','rb')
                des_val = f.read()
                f.close()
                if len(des_val) == 0:
                    list_msg.append('The function "decrypt_file" created an empty file for DES decrypted output')
                f = open('aes_output_e.txt','rb')
                aes_val = f.read()
                f.close()
                if len(aes_val) == 0:
                    list_msg.append('The function "decrypt_file" created an empty file for AES decrypted output')
            else:
                list_msg.append('The function "decrypt_file" does not return 0')
        except Exception as e:
            print(e)
            list_msg.append('The function "decrypt_file" either doesn\'t exist or does not accept the correct number of arguments or has invalid argument type or returned an error')


    except Exception as e:
        list_msg.append('Program import/execution failed')
        print(e)
    if len(list_msg)>0:
        return '\n'.join(list_msg)
    elif len(list_msg) == 0:
        return 'The program has no detectable format errors. Good job.'


if __name__ == '__main__':
    try:
        print(test_script('homework4.py')) # Your program name goes here
    except Exception as e:
        print(e)