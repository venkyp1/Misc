#!/usr/bin/python

import sys, getopt

def usage(progname):
    print("Usage: ")
    print(progname, ' -i <inputfile> -o <outputfile>')
    sys.exit()

def TestArgs(argv):
    
    inputfile = ''
    outputfile = ''

    if len(argv) < 2:
        usage(sys.argv[0])
    try:
        opts, args = getopt.getopt(argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        usage(sys.argv[0])
    for opt, arg in opts:
        if opt == '-h':
            usage(sys.argv[0])
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)
    
if __name__ == "__main__":
   TestArgs(sys.argv)
