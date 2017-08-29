#!/usr/bin/env python

import sys
#Opening file with open

## f = open "/Users/cmdb/data/genomes/BDGP6.fa"

##This is run on the command line using "04-files.py file"
if len (sys.argv)>1:
    f = open( sys.argv[1])
    first_line = f.readline()

##This will read the file and put the first line as an output
##This can be called in the command line using "cat ~file | 04-files.py"
else:
    first_line = sys.stdin.readline()

print first_line