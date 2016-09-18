#!/usr/bin/python3
'''
AES in ECB mode
'''
import base64
from Crypto.Cipher import AES

def decryptECB(cipher, key):
    aes_crypt = AES.new(key, AES.MODE_ECB)
    return aes_crypt.decrypt(cipher)

def main():
    key = b'YELLOW SUBMARINE'
    with open('7.txt') as f:
        fdata = base64.b64decode(f.read())
        print(decryptECB(fdata, key).decode())

if __name__ == "__main__":
    main()
