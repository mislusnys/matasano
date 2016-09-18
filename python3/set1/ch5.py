#!/usr/bin/python3
'''
Implement repeating-key XOR
'''
import binascii

def r_key_xor(m, key):
    return bytes([byte ^ key[i % len(key)] for i, byte in enumerate(m)])

def main():
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    xor_bytes = r_key_xor(message, key)
    xor = binascii.hexlify(xor_bytes).decode()
    print(xor)
    if xor == expected:
        print('It Works!')
    return 0

if __name__ == "__main__":
    main()

