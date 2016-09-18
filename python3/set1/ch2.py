#!/usr/bin/python3
'''
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
'''

import binascii
from Crypto.Util.strxor import strxor

# Do not use Crypto.Util
def fixed_xor_(s1, s2):
    plain1 = binascii.unhexlify(s1)
    plain2 = binascii.unhexlify(s2)
    ba = bytearray()
    for i, j in zip(plain1, plain2):
        ba.append(i ^ j)
    return bytes(ba)

# Use Crypto.Util
def fixed_xor(s1, s2):
    plain1 = binascii.unhexlify(s1)
    plain2 = binascii.unhexlify(s2)
    return strxor(plain1, plain2)

def main():
    a = b'1c0111001f010100061a024b53535009181c'
    b = b'686974207468652062756c6c277320657965'
    print('Expected: 746865206b696420646f6e277420706c6179')
    xor = binascii.hexlify(fixed_xor(a, b)).decode()
    print('From strxor: ', xor)
    xor = binascii.hexlify(fixed_xor_(a, b)).decode()
    print('From custom strxor: ', xor)

if __name__ == "__main__":
    main()

