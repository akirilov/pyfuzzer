#!/usr/bin/python

import os, sys
import math
import random
import shutil
import time

def FuzzString(string, factor):
    '''
    Randomly chooses between 0 and <factor> percent of <string>'s bytes and
    substitutes them with new, random bytes, then returns the resulting string.
    '''
    buf = list(string)
    numwrites = random.randrange(math.ceil((float(len(buf)) * factor)))

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c" % (rbyte)

    return ''.join(buf)

def main():
    # Generate fuzzed file name
    t_orig = sys.argv[1]
    factor = float(sys.argv[2])
    t_name = os.path.splitext(t_orig)[0]
    t_ext = os.path.splitext(t_orig)[1]
    t_fuzz = t_name + '_fuzzed' + t_ext

    # Read original file into string, fuzz, and save
    f_orig = open(t_orig, 'r')
    str_orig = f_orig.read()
    str_fuzz = FuzzString(str_orig, factor);
    f_fuzz = open(t_fuzz, 'w')
    f_fuzz.write(str_fuzz)
    
    # Close files
    f_orig.close()
    f_fuzz.close()
    
    # Start fuzzed file
    os.system('open ' + t_fuzz)

if __name__ == '__main__':
    main()
