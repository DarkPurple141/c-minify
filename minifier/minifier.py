#!/usr/bin/env python3

import sys, random

reserve = [
    'auto',	'else',	'long',	'switch',
    'break', 'enum', 'register', 'typedef',
    'case',	'extern', 'return',	'union',
    'char',	'float', 'short', 'unsigned',
    'const', 'for', 'signed', 'void',
    'continue', 'goto', 'sizeof', 'volatile',
    'default', 'if', 'static', 'while',
    'do', 'int', 'struct', 'double', '#include', '#define'
]

def arg_handling():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            parse(f,arg)
            f.close()

def parse(file_handle, fname):
    """Main handling of the minify parse."""
    var = {}
    output = []
    for line in file_handle:
        line = line.strip()
        if line.startswith('#define') or line.startswith('#include'):
            output.append(line)
            output.append('\n')
            continue
        elif line.startswith('//'):
            continue
        words = line.split()
        for word in words:
            if word in reserve:
                output.append(word)
            else:
                try:
                    new = var[word]
                except KeyError:
                    var[word] = word[0:2]
                    new = var[word]
                output.append(new)
    output = " ".join(output)
    print_output(fname, output)

def print_output(fname, output):
    """Prints output to the same filename with a c bad extension.
    Thus test.c reads out as test.ccbad etc."""
    try:
        with open(fname + "cbad",'w') as fw:
            fw.write(output)
    except OSError:
        print('cannot create file', fname + "cbad")

if __name__ == '__main__':
    arg_handling()
    print("OK.")
