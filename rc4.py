# RC4 Algorithm implementation using python

def Algo(plain_text, key):
    # Key Scheduling
    S_arr = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S_arr[i] + ord(key[i%len(key)])) % 256
        S_arr[i], S_arr[j] = S_arr[j], S_arr[i]

    # Key Stream generation - Pseudo Random Generation Algorithm
    i = 0
    j = 0
    key_num = []
    for q in range(len(plain_text)):
        i = (i + 1) % 256
        j = (j + S_arr[i]) % 256
        S_arr[i], S_arr[j] = S_arr[j], S_arr[i]

        temp = (S_arr[i] + S_arr[j]) % 256
        new_S_arr = S_arr[temp]
        key_num.append(new_S_arr)

    return key_num
# Encryption
def encryption(plain_text,key_num):
    num_message = [ord(char) for char in plain_text]
    cipher_text = ''.join(['{:08b}'.format(i ^ j) for i, j in zip(num_message, key_num)])
    return cipher_text


# Decryption
def decryption(cipher_text,key_num):
    
    num_cipher = [int(cipher_text[i:i + 8], 2) for i in range(0, len(cipher_text), 8)]
    de_plain = ''.join(chr(i ^ j) for i, j in zip(num_cipher, key_num))
    return de_plain



print("Enter Plain Text:")
plain_text = input()

print("Enter Key:")
key = input()

print("Enter the cryptography method\n E - Encryption\n D - Decryption")
Method = input()

key_num = Algo(plain_text, key)
cipher_text = encryption(plain_text,key_num)
de_plain = decryption(cipher_text,key_num)

if(Method == 'E' or Method == 'e'):
    print('Cipher Text:', cipher_text)

elif(Method == 'D' or Method == 'd'):
    print('Cipher Text:', cipher_text)
    print("Enter Cipher Text:")
    cipher_text = input()
    print('Plain Text:', de_plain)
    
else:
    print("Wrong Entry!")


