#!/usr/bin/env python3

import sys

def arg_handling():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            parse(f,arg)
            f.close()

def parse(file_handle, fname):
    """Main handling of the minify parse.
    """
    output = []
    print_output(fname, output)

def print_output(fname, output):
    """Prints output to the same filename with a c bad extension.
    Thus test.c reads out as test.ccbad etc."""
    try:
        with open(fname + "cbad",'w') as fw:
            fw.write("STUFF")
    except OSError:
        print('cannot create file', fname + "cbad")

if __name__ == '__main__':
    arg_handling()
    print("OK.")
