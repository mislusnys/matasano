#!/usr/bin/python3
'''
Detect AES in ECB mode
'''
import itertools

def calc_blocks_in_line(line):
    # 16 byte blocks, 32 chars
    blocks = [line[i:i+32] for i in range(0, len(line), 32)] 
    pairs = itertools.combinations(blocks, 2) 
    same = 0 
    for p in pairs: 
        if p[0] == p[1]: 
            same += 1 
    return same 

def main():
    with open('8.txt') as f:
        for line in f:
            count = calc_blocks_in_line(line)
            if count > 0:
                print("Count:", count, "\nLine:", line)
    
if __name__ == "__main__":
    main()
    
