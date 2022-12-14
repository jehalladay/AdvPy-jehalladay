'''
Check to see if every line of input is the same as the corresponding line of a file
the file is given via the command line

This is used instead of diff since diff doesn't work as expected on Mac
'''

import sys

def main():
    with open(sys.argv[1], 'r') as f:
        for i, line in enumerate(f):
            val = str(input())
            line = str(line).strip('\n')



            if line != val:
                print(f"Found a difference on line: {i}")
                print(f"File: {line}: len: {len(line)}")
                print(f"Input: {val}: len: {len(val)}")
                return
    print("All lines match")

if __name__ == "__main__":
    main()