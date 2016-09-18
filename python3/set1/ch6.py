#!/usr/bin/python3
'''
Break repeating-key XOR
'''
import base64
import itertools
import ch3
import ch5

def h_dist(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(s1, s2))

# Split and transpose blocks
def split_transposed_blocks(cipher, size):
    blocks = []
    for i in range(size):
        blocks.append(cipher[i::size])
    return blocks

# Calculate the key 1 char at a time
def break_rkey_xor(cipher, ksize):
    blocks = split_transposed_blocks(cipher, ksize)
    key = [ch3.break_single_byte_xor(block)[0] for block in blocks]
    return bytes(key)    

# Normalized Distance
def ndist(cipher, ksize):
    # Split into blocks
    n = 4
    blocks = []
    for i in range(n):
        blocks.append(cipher[i*ksize:(i+1)*ksize]) 
    # Calculate distances between pairs
    pairs = list(itertools.combinations(blocks, 2))
    scores = [h_dist(p[0], p[1])/ksize for p in pairs]
    return sum(scores) / len(scores)
    
def main():
    '''
    # Test
    test1 = b'this is a test'
    test2 = b'wokka wokka!!!'
    print(h_dist(test1, test2))
    '''
    with open('6.txt') as f:
        fdata = base64.b64decode(f.read())
        # Find Min Distance (calculate KEYSIZE)
        ksize = min([i for i in range(2, 41)], key=lambda p: ndist(fdata, p))
        print('Key size:', ksize)
        key = break_rkey_xor(fdata, ksize)
        print("Key:", key.decode())
        decoded = ch5.r_key_xor(fdata, key).decode()
        print("Decoded Text:\n", decoded)

if __name__ == "__main__":
    main()

