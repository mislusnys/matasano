#!/usr/bin/python3
import ch3

def main():
    with open("4.txt") as f:
        lines = [bytes.fromhex(l.strip()) for l in f if l != '\n']
        max_t = max([ch3.break_single_byte_xor(line)[1] for line in lines], key=lambda p: ch3.text_score(p))

    print('Max Score Plain Text:', max_t.decode())
    
if __name__ == "__main__":
    main()

