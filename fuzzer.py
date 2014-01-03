#!/usr/bin/python

import math
import random

def FuzzString(string, factor):
    '''
    Randomly chooses between 0 and <factor> percent of <string>'s bytes and
    substitutes them with new, random bytes, then returns the resulting string.
    '''
    buf = list(string)
    numwrites = random.randrange(math.ceil((float(len(buf)) * factor / 100)))

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c" % (rbyte)

    return ''.join(buf)

def main():
    # test the fuzzer
    print FuzzString("hello world", 50)

if __name__ == '__main__':
    main()
