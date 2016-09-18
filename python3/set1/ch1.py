#!/usr/bin/python3
'''
Convert hex to base64
'''

import binascii
import base64

def hex_to_base64(s):
    plain = binascii.unhexlify(s)
    return base64.b64encode(plain)

def main():
    x = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print('Expected: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    print('Result:', hex_to_base64(x).decode())

if __name__ == "__main__":
    main()


